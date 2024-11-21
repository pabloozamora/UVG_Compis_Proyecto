from IntermediateCodeGenerator import ThreeAddressInstruction, PrintInstruction, Label, JumpInstruction, ParamInstruction, ArgInstruction, CallInstruction, ReturnInstruction, EndFunctionInstruction
from SymbolTable import Symbol, TempSymbol, NumberType, AnyType, StringType, InstanceType

DATA_BP = 0x10000000

class AddressDescription:
    def __init__(self, symbol, address=None, offset=0, ambiguous=False):
        self.symbol_id = symbol.id
        self.name = symbol.name
        self.registers = []
        self.address = address
        self.address_valid = False
        self.offset = offset
        self.ambiguous = ambiguous

class MIPSGenerator:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.mips_code = []
        self.subroutines = []
        self.register_descriptor = {
            't0': None,'t1': None, 't2': None, 't3': None, 't4': None, 't5': None, 't6': None, 't7': None,
        }
        self.address_descriptor = {}
        self.current_instruction_register = None
        self.ambiguous_region = False
        self.ambiguous_region_exit = None
        self.in_subroutine = False
        self.subroutine_label = None
        self.current_stack = []
        self.calling_subroutine = None
        self.return_symbol = None
        self.current_function_max_offset = 0
        self.a_count = 0
        self.are_strings = []
        
    def add_code(self, code):
        if not self.in_subroutine:
            self.mips_code.append(code)
            
        else:
            self.subroutines[-1].append(code)
        
    def set_ambiguous_region_exit(self, label):
        # Se terminó la primera mitad de la región ambigua, resetear el descriptor de registros y el descriptor de direcciones
        self.ambiguous_region_exit = label
        self.reset_registers()
        
    def check_ambiguous_region(self, label):
        if label == self.ambiguous_region_exit:
            # Se terminó la región ambigua, resetear el descriptor de registros y el descriptor de direcciones
            self.ambiguous_region = False
            self.ambiguous_region_exit = None
            self.reset_registers()
            
    def reset_after_subroutine(self):
        self.register_descriptor = {
            't0': None,'t1': None, 't2': None, 't3': None, 't4': None, 't5': None, 't6': None, 't7': None,
        }
        for name, variable in self.address_descriptor.items():
            variable.registers = []
        
    def reset_registers(self):
        
        # Guardar en el heap los valores de los registros que no tienen su último valor válido en memoria
        for name, variable in self.address_descriptor.items():
    
            if not variable.address_valid: # Si la variable no tiene su último valor válido en memoria
                # Cargar la dirección del heap de la variable en un registro
                self.add_code(f"lw $a3, {variable.address} # Guardar variables antes de ambiguedad")
                self.add_code(f"sw ${variable.registers[0]}, {variable.offset}($a3)")
                variable.address_valid = True
                
            # Indicar en el descriptor de direcciones que la variable ya no tiene su último valor válido en ningún registro, sino en el heap
            variable.registers = []
            
        # Limpiar el descriptor de registros de variables ambiguas
        address_descriptor_without_ambiguous = {key: value for key, value in self.address_descriptor.items() if not value.ambiguous}
        
        self.address_descriptor = address_descriptor_without_ambiguous
        
        self.register_descriptor = {
            't0': None,'t1': None, 't2': None, 't3': None, 't4': None, 't5': None, 't6': None, 't7': None,
        }
        
        return
        
    def allocate_memory(self, symbol, instance=False):
        if not self.address_descriptor.get(symbol.id): # Si la variable no está en el descriptor de direcciones, se debe asignar una dirección del heap
            # Pendiente: Determinar si el scope GP o SP
            # GP
            data_address = hex(DATA_BP + symbol.offset) # Calcular la dirección en la sección de data según el offset de la variable
            
            # Si se está dentro de una región ambigua, no se guarda en el descriptor de direcciones, ya que podría ejecutarse o no
            # Por tanto, se debe volver a chequear si la variable ya está en memoria estática
            self.address_descriptor[symbol.id] = AddressDescription(symbol, data_address, ambiguous=self.ambiguous_region) # Guardar la dirección en el descriptor de direcciones
            
            # Si es un valor de retorno, puede tener varios tipos
            if isinstance(symbol.type, set):
                type = symbol.type
                if len(type) == 0:
                    type = NumberType(is_float=True)
                else:
                    type = type.pop()
                
            else:
                type = symbol.type
                
            if instance:
                # Las instancias ya tienen un espacio en el heap asignado
                return
            
            # Saltar a la subrutina para revisar si la variable ya está en memoria estática
            # Preparar los argumentos para la subrutina
            self.add_code(f"li $a1, {data_address} # Cargar la direccion asignada para la variable '{symbol.name}' en memoria estatica")
            self.add_code(f"li $a2, {type.size} # Cargar los bytes que necesita del heap")
            self.add_code('jal check_existing_variable')
        
        return
        
    def load_constant(self, constant, dest=None):
        
        # Determinar el tipo de constante
        
        # Si es una cadena
        if isinstance(constant, str):
            
            # Si se está cargando dentro de una función, cargar la cadena en el stack
            if dest.scope == 'SP':
                
                # Las cadenas no caben en el stack, se deben almacenar en el heap
                
                # Llamar a subrutina para alojar memoria en el heap y retornar la dirección de memoria asignada
                self.add_code(f"li $s0, 255 # Tamano de la cadena a copiar")
                self.add_code("jal alloc_memory # Reservar espacio en el heap para la cadena")
                
                # Obtener un registro base para cargar la dirección del stack de la variable
                base_register = self.get_reg('$fp')['register']
                
                self.add_code(f"addi ${base_register}, $fp, {dest.offset + 8} # La direccion del stack de la variable '{dest.name}' se carga en ${base_register}")
                
                # Almacenar la dirección de memoria de la cadena en el stack
                self.add_code(f"sw $s1, 0(${base_register}) # Almacenar la direccion de memoria de la cadena '{dest.name}' en el stack")
                
                # Cargar la dirección de memoria de la cadena en un registro
                self.add_code(f"lw ${base_register}, 0(${base_register}) # La direccion de memoria de la cadena '{dest.name}' se carga en ${base_register}")
                
                # Actualizar el descriptor de registros
                self.register_descriptor[base_register] = f'{dest.name}[{dest.offset + 8}]'
                
                # Obtener un registro disponible para cargar los bytes de la cadena
                char_reg = self.get_reg(constant)['register']
                
                # Almacenar la cadena carácter por carácter
                for i, char in enumerate(constant):
                    char_ascii = ord(char)  # Convertir el carácter a su valor ASCII
                    self.add_code(f'li ${char_reg}, {char_ascii}  # Cargar ASCII del caracter "{char}" en ${char_reg}')
                    self.add_code(f'sb ${char_reg}, {i}(${base_register})  # Guardar el caracter en la direccion {i}({dest.offset + 8})')
                    
                # Agregar el terminador nulo al final de la cadena
                self.add_code(f'li ${char_reg}, 0  # Terminador nulo')
                self.add_code(f'sb ${char_reg}, {len(constant)}(${base_register}) # Guardar terminador nulo')
                
                # Actualizar el descriptor de registros
                self.register_descriptor[char_reg] = char
                
                return
            
            # Obtener la dirección de memoria de la variable
            address = self.address_descriptor[dest.id].address
            
            # Obtener un registro disponible para cargar los bytes de la cadena
            char_reg = self.get_reg(constant)['register']
            
            # Obtener un registro base para cargar la dirección de memoria de la variable
            base_register = self.get_reg(address)['register']
            self.add_code(f"lw ${base_register}, {address} # La direccion del heap de la variable '{dest.name}' se carga en ${base_register}")
            
            # Actualizar el descriptor de registros
            self.register_descriptor[base_register] = address
            
            # Almacenar la cadena carácter por carácter
            for i, char in enumerate(constant):
                char_ascii = ord(char)  # Convertir el carácter a su valor ASCII
                self.add_code(f'li ${char_reg}, {char_ascii}  # Cargar ASCII del caracter "{char}" en ${char_reg}')
                self.add_code(f'sb ${char_reg}, {i}(${base_register})  # Guardar el caracter en la direccion {i}({address})')

            # Agregar el terminador nulo al final de la cadena
            self.add_code(f'li ${char_reg}, 0  # Terminador nulo')
            self.add_code(f'sb ${char_reg}, {len(constant)}(${base_register})  # Guardar terminador nulo')
            
            # Cargar la cadena en un registro
            self.add_code(f"lw ${char_reg}, 0(${base_register}) # El valor de la variable '{dest.name}' en el heap se carga en ${char_reg}")
            
            # Actualizar el descriptor de registros
            self.register_descriptor[char_reg] = char
            
            # Actualizar el descriptor de direcciones
            self.address_descriptor[dest.id].registers.append(base_register)
            
            return base_register
        
        # Si es un float
        if isinstance(constant, float):
            constant = float(constant)
            self.add_code(f"li.s $f1, {constant}")
            
            # Obtener un registro disponible para mover el valor del registro float al registro entero
            register = self.get_reg(constant)
            
            # Mover el valor del registro float al registro entero
            self.add_code(f"mfc1 ${register['register']}, $f1")
            
            return register['register']
        
        if isinstance(constant, int):
            constant = int(constant)
            
            # Obtener un registro disponible para cargar la constante
            register = self.get_reg(constant)
            
            self.add_code(f"li ${register['register']}, {constant}")
            
            return register['register']
    
    # Param offset: Si no se envía un offset, únicamente se devuelve la dirección de memoria de la variable
    def load_variable(self, symbol, offset=None, instance=False):
        
        if symbol.scope == 'SP':
            function_register = self.get_reg(symbol.id)['register']
            self.add_code(f'lw ${function_register}, {symbol.offset + 8}($fp) # Obtener el valor de la variable "{symbol.name}" del stack')
            
            # Actualizar el descriptor de registros
            self.register_descriptor[function_register] = symbol.id
            
            if offset is not None:
                self.add_code(f'lw ${function_register}, {offset}(${function_register}) # Obtener el valor de la propiedad {offset} de la variable "{symbol.name}" del heap')
                
                # Actualizar el descriptor de registros
                self.register_descriptor[function_register] = f'{symbol.id}[{offset}]'
            
            return function_register
        
        if offset is None:
            offset = 0
        
        # Primero verificar si la variable destino ya tiene una dirección asignada
        self.allocate_memory(symbol) # Si no está en el descriptor de direcciones, se debe asignar una dirección del heap
        
        # Verificar si la variable tiene su último valor válido en algún registro
        if len(self.address_descriptor[symbol.id].registers) > 0:
            return self.address_descriptor[symbol.id].registers[0]
        
        # Obtener la dirección de memoria de la variable
        address = self.address_descriptor[symbol.id].address
        
        # Obtener un registro disponible para cargar la dirección de la variable
        register = self.get_reg(address)
        
        address_reg = register['register']
        address_already_loaded = register['already_loaded']
        
        if not address_already_loaded: # Si la dirección de la variable no estaba en un registro, se debe cargar en un registro
        
            # Cargar la dirección en el heap de la variable en el registro
            self.add_code(f"lw ${address_reg}, {address} # La direccion del heap de la variable '{symbol.name}' se carga en ${address_reg}")
        
        # Actualizar el descriptor de registros
        self.register_descriptor[address_reg] = address
        
        if instance:
            
            # Actualizar el descriptor de direcciones
            self.address_descriptor[symbol.id].registers.append(address_reg)
            
            return address_reg
        
        # Obtener un registro disponible para guardar el valor de la variable
        value_reg = self.get_reg(symbol.id)['register']
        
        # Cargar el valor de la dirección del heap en el registro
        self.add_code(f"lw ${value_reg}, {offset}(${address_reg}) # El valor de la variable '{symbol.name}' en el heap se carga en ${value_reg}")
        
        # Actualizar el descriptor de registros
        self.register_descriptor[value_reg] = symbol.id
        
        # Actualizar el descriptor de direcciones
        self.address_descriptor[symbol.id].registers.append(value_reg)
        
        return value_reg
        
    def get_reg(self, symbol_id):
    
        # Arreglo de registros disponibles
        available_registers = []
        
        # Primero, se verifica si la variable ya está en un registro
        
        for reg, value in self.register_descriptor.items():
            
            if value is symbol_id: # Si la variable ya está en un registro, se retorna el registro
                return {'register': reg, 'already_loaded': True}
            
            if value is None:
                available_registers.append(reg)
            
        # Si no está en un registro, se verifica si hay registros disponibles
        
        if available_registers:
            
            # Actualizar el descriptor de registros
            self.register_descriptor[available_registers[0]] = symbol_id
            
            return {'register': available_registers[0], 'already_loaded': False}
        
        # Si no hay registros disponibles, se debe hacer un reemplazo
        
        variables_not_in_memory = []
        
        # Opción 1: Verificar si hay variables que tienen su último valor válido en memoria
        
        # Si se está en una subrutina, se pueden limpiar los registros, siempre y cuando no se estén utilizando para una instrucción
            
        for reg, value in self.register_descriptor.items():
                
                if reg == self.current_instruction_register: # Si ya se reservó un registro para la instrucción actual no se puede reemplazar
                    continue
                
                self.register_descriptor[reg] = None
                
        self.get_reg(symbol_id)
        
        for reg, value in self.register_descriptor.items():
            
            if reg == self.current_instruction_register: # Si ya se reservó un registro para la instrucción actual no se puede reemplazar
                continue
            
            # Verificar si la variable tiene su último valor válido en memoria
            current_variable = self.address_descriptor.get(value)
            
            # La variable no tiene su último valor válido en memoria (y no es una constante, o sea address_descriptor[value] no es None)
            if current_variable and not current_variable.address_valid:
                variables_not_in_memory.append(value)
                
            # La variable tiene su último valor válido en memoria
            else:
                
                # Hacer pop del registro del listado de registros en los que estaba la variable (Si no está en el listado, no pasa nada)
                if current_variable and reg in current_variable.registers:
                    current_variable.registers.remove(reg)
                
                # Actualizar el descriptor de registros con la nueva variable
                self.register_descriptor[reg] = symbol_id
                
                return {'register': reg, 'already_loaded': False}
            
        # Opción 2: Utilizar alguna de las variables que no tienen su último valor válido en memoria
        
        if variables_not_in_memory:
            
            # Seleccionar la variable que se usó menos recientemente
            variable_to_replace = variables_not_in_memory[0]
            
            # Obtener el registro en el que se encuentra la variable
            register_to_replace = None
            for reg, value in self.register_descriptor.items():
                if value is variable_to_replace:
                    register_to_replace = reg
                    break
            
            # Actualizar el descriptor de registros con la nueva variable
            self.register_descriptor[register_to_replace] = symbol_id
            
            # Retornar el registro que se debe reemplazar y agregar la instrucción para almacenar el valor de la variable reemplazada en el heap
            
            # Se necesitan dos registros para hacer el reemplazo
            temp_reg =  temp_reg = next(reg for reg in self.register_descriptor.keys() if reg != register_to_replace)
            self.add_code(f'addi, $sp, $sp, -4 # Reservar espacio en el stack para almacenar el valor de temp_reg')
            self.add_code(f'sw ${temp_reg}, 0($sp) # Guardar el valor de temp_reg en el stack')
            
            # Cargar la dirección del heap de la variable en un registro
            self.add_code(f"lw $t0, {self.address_descriptor[variable_to_replace].address}")
            self.add_code(f"sw {register_to_replace}, {self.address_descriptor[variable_to_replace].offset}(${temp_reg})")
            
            # Recuperar temp_reg del stack
            self.add_code(f'lw ${temp_reg}, 0($sp) # Recuperar el valor de temp_reg del stack')
            self.add_code(f'addi, $sp, $sp, 4 # Liberar espacio en el stack')
            
            # Indicar en el descriptor de direcciones que la variable ya no tiene su último valor válido en el registro, sino en el heap
            self.address_descriptor[variable_to_replace].registers.remove(register_to_replace)
            self.address_descriptor[variable_to_replace].address_valid = True
            
            return {'register': register_to_replace, 'already_loaded': False}
        
        return None
    
    def copy_string(self, src_reg, dest_reg, start_offset):
        pass
    
    def write_code(self, file_name='./output/output.asm'):
        with open(file_name, 'w') as file:
            
            file.write(".data\n")
            file.write("newline: .asciiz \"\\n\"\n")
            
            file.write(".text\n")
            file.write(".globl main\n")
            file.write("main:\n")
            
            for line in self.mips_code:
                file.write(f"{line}\n")
                
            file.write("li $v0, 10\n")
            file.write("syscall\n")
            
            # Escribir las subrutinas
            for subroutine in self.subroutines:
                file.write('\n')
                for line in subroutine:
                    file.write(f"{line}\n")
            
            # Subrutina para revisar si la variable ya está en memoria estática
            # s0: Dirección de la variable en memoria estática
            # s1: Tamaño de la variable
            
            file.write('\ncheck_existing_variable:\n')
            file.write('lw $s0, 0($a1) # Cargar la direccion de la variable en memoria estatica\n')
            file.write('bnez $s0, end_check_existing_variable # Si la direccion (argumento 1) no es 0, regresar\n')
            file.write('save_variable:\n')
            file.write(f"li $v0, 9\n")
            file.write(f"move $a0, $a2 # Obtener el tamano de la variable del argumento 2\n")
            file.write("syscall\n")
            file.write(f"move $a2, $v0 # Guardar la direccion de memoria asignada en $a2\n")
            file.write("sw $a2, 0($a1) # Guardar la direccion de memoria asignada en la variable en memoria estatica\n")
            file.write('end_check_existing_variable:\n')
            file.write('jr $ra\n')
            
            # Subrutina para alojar memoria en el heap y retornar la dirección de memoria asignada
            # s0: Tamaño de la memoria a alojar
            # s1: Dirección de memoria asignada
            file.write('\nalloc_memory:\n')
            file.write('li $v0, 9\n')
            file.write('move $a0, $s0\n')
            file.write('syscall\n')
            file.write('move $s1, $v0\n')
            file.write('jr $ra\n')
            
            # Subrutina para concatenar dos cadenas
            # s0: Dirección de la cadena fuente
            # s1: Offset inicial de la cadena fuente
            # s3: Dirección de la cadena destino
            file.write('\ncopy_string:\n')
            file.write(f"copy_loop:\n")
            file.write(f"lb $s2, 0($s0)    # Leer caracter de la cadena fuente\n")
            file.write(f"beqz $s2, end_copy # Si el caracter es nulo, terminar\n")
            file.write(f"add $s4, $s3, $s1 # Calcular la direccion efectiva\n")
            file.write(f"sb $s2, 0($s4)    # Escribir el caracter en la cadena destino\n")
            file.write(f"addi $s0, $s0, 1  # Avanzar en la cadena fuente\n")
            file.write(f"addi $s1, $s1, 1  # Avanzar en la cadena destino\n")
            file.write(f"j copy_loop               # Continuar con el siguiente caracter\n")
            file.write(f"end_copy:\n")
            file.write(f"jr $ra\n")
        
    def generate(self):
        for i, instruction in enumerate(self.intermediate_code):
            if isinstance(instruction, ThreeAddressInstruction):
                if instruction.op == '=':
                    self.assign(instruction)
                elif instruction.op == 'ADD':
                    self.addInt(instruction)
                elif instruction.op == 'SUB':
                    self.subInt(instruction)
                elif instruction.op == 'MUL':
                    self.mulInt(instruction)
                elif instruction.op == 'DIV':
                    self.divInt(instruction)
                elif instruction.op == 'MOD':
                    self.mod(instruction)
                elif instruction.op == 'ASSIGN':
                    self.assign(instruction)
                elif instruction.op == 'LABEL':
                    self.label(instruction)
                elif instruction.op == 'PRINT':
                    self.print(instruction)
                elif instruction.op == 'READ':
                    self.read(instruction)
                elif instruction.op == 'ALLOC':
                    self.alloc(instruction)
                elif instruction.op == 'CONCAT':
                    self.concat(instruction)
                    
            elif isinstance(instruction, PrintInstruction):
                self.print(instruction)
                
            elif isinstance(instruction, Label):
                
                # Si es una label de función
                if instruction.func:
                
                    # Buscar la instrucción endfunc con el offset máximo de la función
                    
                    function_name = instruction.function_name
                    endfunc = None
                    
                    j = i
                    while j < len(self.intermediate_code):
                        current_instruction = self.intermediate_code[j]
                        if isinstance(current_instruction, EndFunctionInstruction):
                            current_instruction_function_name = current_instruction.function_name
                            if current_instruction_function_name == function_name:
                                endfunc = current_instruction
                                break
                        j += 1
                        
                    self.current_function_max_offset = endfunc.max_offset + 4
                
                self.label(instruction)
                
            elif isinstance(instruction, JumpInstruction):
                self.jump(instruction)
                
            elif isinstance(instruction, CallInstruction):
                self.call(instruction)
                
            elif isinstance(instruction, ReturnInstruction):
                self.return_(instruction)
                
            elif isinstance(instruction, EndFunctionInstruction):
                self.end_function(instruction)
                
            elif isinstance(instruction, ParamInstruction):
                self.param(instruction)
        
        self.write_code()
        
    def assign(self, instruction):
        dest = instruction.dest
        value = instruction.arg1
        
        if value == 'R':
            
            if dest.scope == 'SP':
                # Resetear el descriptor de registros
                self.reset_registers()
                
                dest_reg = self.get_reg(dest.id)['register']
                self.add_code(f'move ${dest_reg}, $v0 # Obtener el valor de retorno de la funcion')
                
                # Almacenar el valor en la dirección del stack de la variable destino
                self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el valor de retorno de la funcion en el stack")
                
                return
            
            # Obtener un registro para guardar el valor de retorno de la función
            dest_reg = self.get_reg(dest.id)['register']
            #self.add_code(f"lw ${dest_reg}, {self.stack_sizes[self.calling_subroutine]}($sp)  # Leer el valor de retorno desde la ultima posicion")
            self.add_code(f"move ${dest_reg}, $v0  # Leer el valor de retorno desde la ultima posicion")
            
            self.allocate_memory(dest) # Verificar si la variable destino ya tiene una dirección asignada
            
            # Restaurar el stack a la posición de $fp después de la llamada
            self.add_code(f"move $fp, $sp # Liberar espacio de variables locales y $ra")
            
            # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
            self.address_descriptor[dest.id].registers = [dest_reg] # Último valor válido de la variable destino ahora es el valor de la variable value
            self.address_descriptor[dest.id].address_valid = False
            
            return
            
        # Si el scope de la variable destino es SP
        
        if dest.scope == 'SP':
            
            # Verificar si el valor a asignar es una variable o una constante
            if isinstance(value, Symbol):
                value_reg = self.load_variable(value, offset=instruction.argOffset)
                
            else:
                
                 # Si es una constante, cargar su valor en un registro
                if isinstance(value, str):
                    
                    # Si es una cadena, se necesita la variable destino para almacenar la dirección de memoria de la cadena
                    value_reg = self.load_constant(value, dest)
                    return
                    
                else:
                    value_reg = self.load_constant(value)
                    
            if instruction.offset != None:
                
                # Obtener un registro base para cargar la dirección del heap de la variable
                base_register = self.get_reg('$fp')['register']
                self.add_code(f"lw ${base_register}, {dest.offset + 8}($fp) # La direccion del stack de la variable '{dest.name}' se carga en ${base_register}")
                
                # Actualizar el descriptor de registros
                self.register_descriptor[base_register] = f'{dest.name}[{dest.offset + 8}]'
                
                self.add_code(f"sw ${value_reg}, {instruction.offset}(${base_register}) # Almacenar el valor de la variable '{dest.name}' en el heap")
                
                return
            
            # Almacenar el valor en la dirección del stack de la variable destino
            self.add_code(f"sw ${value_reg}, {dest.offset + 8}($fp) # guardar el valor de la variable '{dest.name}' en el stack")
            
            self.return_symbol = dest
            
            return
        
        if value is None: # Si no se trata de una asignación, sino de una declaración de variable, solo se debe reservar la memoria en el heap
            self.current_instruction_register = None
            return
        
         # El último valor válido de la variable destino ahora debe apuntar al último valor válido de la variable value
        
        if isinstance(value, Symbol) and isinstance(value.type, InstanceType) and instruction.argOffset is not None:
            # Las propiedades de instancias tienen un tamaño fijo de 4 bytes
            dest.type = NumberType()
        
        self.allocate_memory(dest, instance=isinstance(dest.type, InstanceType)) # Verificar si la variable destino ya tiene una dirección asignada
        
        # Verificar si el valor a asignar es una variable o una constante
        if isinstance(value, Symbol):
            
            # Si se está accediendo a una propiedad de la instancia, se debe cargar el valor de la propiedad en un registro
            if isinstance(value.type, InstanceType) and instruction.argOffset is not None:
                
                # Registro para obtener la dirección del heap de la instancia
                value_reg = self.load_variable(value, instance=True)
                
                # Registro para guardar el valor de la propiedad de la instancia
                dest_reg = self.get_reg(dest.id)['register']
                
                # Actualizar el descriptor de registros
                self.register_descriptor[dest_reg] = dest.id
                
                # Cargar el valor de la propiedad de la instancia en el registro
                self.add_code(f"lw ${dest_reg}, {instruction.argOffset}(${value_reg}) # Cargar el valor de la propiedad de la instancia '{value.name}' en ${value_reg}")
                
                # Inferencia de tipos
                
                if value.type.class_type.fields:
                    
                    field_name = None
                    field_type = None
                    
                    for field, details in value.type.class_type.fields.items():
                        if details['offset'] == instruction.argOffset:
                            field_name = field
                            field_type = details['type']
                            break
                        
                    if field_type and (isinstance(field_type, AnyType) or isinstance(field_type, StringType)):
                        self.are_strings.append(dest.id)
                
                # Actualizar el descriptor de registros
                self.register_descriptor[value_reg] = f'{value.id}[{instruction.argOffset}]'
                
                # Actualizar el descriptor de direcciones
                self.address_descriptor[dest.id].registers = [dest_reg]
                
                return
            
            # Se asigna una instancia a otra instancia
            elif isinstance(value.type, InstanceType):
                # Obtener la dirección del heap de la instancia value
                value_address = self.address_descriptor[value.id].address
                
                # Obtener un registro base para cargar la dirección de memoria de la instancia
                base_register = self.get_reg(value_address)['register']
                
                # Cargar la dirección de memoria de la instancia value en el registro
                self.add_code(f"lw ${base_register}, {value_address} # La direccion del heap de la instancia '{value.name}' se carga en ${base_register}")
                
                # Actualizar el descriptor de registros
                self.register_descriptor[base_register] = value_address
                
                dest_address = self.address_descriptor[dest.id].address
                
                # Obtener un registro base para cargar la dirección de memoria de la variable destino
                dest_reg = self.get_reg(dest_address)['register']
                
                # Cargar la dirección de memoria de la variable destino en el registro
                self.add_code(f"li ${dest_reg}, {dest_address} # La direccion de memoria estatica de la variable '{dest.name}' se carga en ${dest_reg}")
                
                # Actualizar el descriptor de registros
                self.register_descriptor[dest_reg] = dest_address
                
                # Almacenar la dirección de memoria de la instancia en dest
                self.add_code(f"sw ${base_register}, 0(${dest_reg}) # Almacenar la direccion de memoria de la instancia '{value.name}' en la variable '{dest.name}'")
                
                # Actualizar el descriptor de direcciones
                self.address_descriptor[dest.id].registers = [base_register]
                
                return
            
            else:
                
                # Si es una variable, ya está en el descriptor de direcciones, cargar su valor verdadero en un registro
                value_reg = self.load_variable(value)
            
        else:
            
            # Si es una constante, cargar su valor en un registro
            if isinstance(value, str):
                
                # Si es una cadena, se necesita la variable destino para almacenar la dirección de memoria de la cadena
                value_reg = self.load_constant(value, dest)
                
            else:
                value_reg = self.load_constant(value)
            
        # Almacenar el valor en la dirección del heap de la variable destino
        # self.add_code(f"sw ${value_reg}, 0(${dest_reg})") # Si el valor debe cargarse de un offset de la variable, indicarlo
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[dest.id].registers = [value_reg] # Último valor válido de la variable destino ahora es el valor de la variable value
        self.address_descriptor[dest.id].address_valid = False
    
    def add(self, instruction):
        
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{instruction.arg1.name}' en un registro float")
        self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{instruction.arg2.name}' en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.add_code("add.s $f3, $f1, $f2")
        
        dest = instruction.dest
        
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.add_code(f"mfc1 ${dest_reg}, $f3 # Mover el resultado de la suma a un registro entero")
        
        if dest.scope == 'SP':
            
            # Almacenar el valor en la dirección del stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la suma a la posicion del stack de {dest.name}")
            
            return
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.add_code(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def addInt(self, instruction):
        # Obtener los registros de las variables de entrada (siempre son temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Liberar el registro de arg1 (si no es necesario mantenerlo)
        self.current_instruction_register = None

        dest = instruction.dest

        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        
        # Realizar la suma de enteros
        self.add_code(f"add ${dest_reg}, ${arg1_reg}, ${arg2_reg} # Sumar los valores de {instruction.arg1.name} y {instruction.arg2.name}")
        
        if dest.scope == 'SP':
            # Almacenar el resultado en el stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la suma en {dest.name}")
            return

        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)

        # Actualizar el descriptor de direcciones para indicar que la variable destino
        # ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
    
    def sub(self, instruction):
       # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{instruction.arg1.name}' en un registro float")
        self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{instruction.arg2.name}' en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.add_code("sub.s $f3, $f1, $f2")
        
        dest = instruction.dest
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.add_code(f"mfc1 ${dest_reg}, $f3")
        
        if dest.scope == 'SP':
            
            # Almacenar el valor en la dirección del stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la suma a la posicion del stack de {dest.name}")
            
            return
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.add_code(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def subInt(self, instruction):
        # Obtener los registros de las variables de entrada (siempre son temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Liberar el registro de arg1 (si no es necesario mantenerlo)
        self.current_instruction_register = None

        dest = instruction.dest

        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        
        # Realizar la resta de enteros
        self.add_code(f"sub ${dest_reg}, ${arg1_reg}, ${arg2_reg} # Restar los valores de {instruction.arg1.name} y {instruction.arg2.name}")
        
        if dest.scope == 'SP':
            # Almacenar el resultado en el stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la resta en {dest.name}")
            return

        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)

        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def mul(self, instruction):
       # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{instruction.arg1.name}' en un registro float")
        self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{instruction.arg2.name}' en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.add_code("mul.s $f3, $f1, $f2")
        
        dest = instruction.dest
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.add_code(f"mfc1 ${dest_reg}, $f3")
        
        if dest.scope == 'SP':
            
            # Almacenar el valor en la dirección del stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la suma a la posicion del stack de {dest.name}")
            
            return
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def mulInt(self, instruction):
        # Obtener los registros de las variables de entrada (siempre son temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Liberar el registro de arg1 (si no es necesario mantenerlo)
        self.current_instruction_register = None

        dest = instruction.dest

        # Obtener un registro para guardar el resultado de la multiplicación
        dest_reg = self.get_reg(instruction.dest.id)['register']
        
        # Realizar la multiplicación de enteros
        self.add_code(f"mul ${dest_reg}, ${arg1_reg}, ${arg2_reg} # Multiplicar los valores de {instruction.arg1.name} y {instruction.arg2.name}")
        
        if dest.scope == 'SP':
            # Almacenar el resultado en el stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la multiplicacion en {dest.name}")
            return

        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)

        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
        
    def div(self, instruction):
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{instruction.arg1.name}' en un registro float")
        self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{instruction.arg2.name}' en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.add_code("div.s $f3, $f1, $f2")
        
        dest = instruction.dest
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.add_code(f"mfc1 ${dest_reg}, $f3")
        
        if dest.scope == 'SP':
            
            # Almacenar el valor en la dirección del stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la division a la posicion del stack de {dest.name}")
            
            return
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.add_code(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def divInt(self, instruction):
        # Obtener los registros de las variables de entrada (siempre son temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Liberar el registro de arg1 (si no es necesario mantenerlo)
        self.current_instruction_register = None

        dest = instruction.dest

        # Obtener un registro para guardar el resultado de la multiplicación
        dest_reg = self.get_reg(instruction.dest.id)['register']
        
        # Realizar la multiplicación de enteros
        self.add_code(f"div ${arg1_reg}, ${arg2_reg} # Dividir los valores de {instruction.arg1.name} y {instruction.arg2.name}")
        
        self.add_code(f"mflo ${dest_reg} # Obtener el cociente de la division")
        
        if dest.scope == 'SP':
            # Almacenar el resultado en el stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado de la division en {dest.name}")
            return

        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)

        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def mod(self, instruction):
        # Obtener los registros de las variables de entrada (siempre son temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Liberar el registro de arg1 (si no es necesario mantenerlo)
        self.current_instruction_register = None

        dest = instruction.dest

        # Obtener un registro para guardar el resultado de la multiplicación
        dest_reg = self.get_reg(instruction.dest.id)['register']
        
        # Realizar la multiplicación de enteros
        self.add_code(f"div ${arg1_reg}, ${arg2_reg} # Dividir los valores de {instruction.arg1.name} y {instruction.arg2.name}")
        
        self.add_code(f"mfhi ${dest_reg} # Obtener el residuo de la division")
        
        if dest.scope == 'SP':
            # Almacenar el resultado en el stack de la variable destino
            self.add_code(f"sw ${dest_reg}, {dest.offset + 8}($fp) # Almacenar el resultado del modulo en {dest.name}")
            return

        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)

        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers = [dest_reg]
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def print(self, instruction):
        arg = instruction.arg
        
        if arg.scope == 'GP':
            # Cargar el valor de la variable a imprimir en un registro
            arg_reg = self.load_variable(arg)
            
        else:
            arg_reg = self.get_reg(arg.id)['register']
            self.add_code(f'lw ${arg_reg}, {arg.offset + 8}($fp) # Cargar la dirección en el stack de la variable "{arg.name}"')
        
        # Validar si el tipo de la variable es float
        #if (isinstance(arg.type, NumberType) and arg.type.is_float) or isinstance(arg.type, AnyType):
        # Mover el valor la variable a un registro float
        
        # PARA FLOATS
        """ self.add_code(f"mtc1 ${arg_reg}, $f1")
        
        # Imprimir el valor de la variable
        self.add_code("li $v0, 2")
        self.add_code("mov.s $f12, $f1")
        self.add_code("syscall # Imprimir") """
        
        # PARA STRINGS
        if isinstance(arg.type, StringType) or arg.id in self.are_strings:
            self.add_code(f"li $v0, 4       # Codigo de syscall para imprimir cadenas")
            self.add_code(f"move $a0, ${arg_reg}  # Mover el valor de la cadena al registro $a0")
            self.add_code("syscall         # Imprimir la cadena")
            
            # Imprimir salto de línea
            self.add_code(f"la $a0, newline # Cargar la dirección de la cadena '\\n'")
            self.add_code("li $v0, 4       # Codigo de syscall para imprimir cadenas")
            self.add_code("syscall         # Imprimir salto de linea")
            
            return
        
        # PARA ENTEROS
        # Imprimir el valor de la variable (entero)
        self.add_code("li $v0, 1       # Codigo de syscall para imprimir enteros")
        self.add_code(f"move $a0, ${arg_reg}  # Mover el valor del entero al registro $a0")
        self.add_code("syscall         # Imprimir el valor en $a0")
        
        # Imprimir salto de línea
        self.add_code(f"la $a0, newline # Cargar la direccion de la cadena '\\n'")
        self.add_code("li $v0, 4       # Codigo de syscall para imprimir cadenas")
        self.add_code("syscall         # Imprimir salto de linea")

            
    def label(self, instruction):
        if instruction.func:
            self.in_subroutine = True
            self.subroutines.append([])
            label = instruction.name
            self.subroutine_label = label
            self.add_code(f"{label}:")
            
            # Prologo de la función
            self.add_code("addi $sp, $sp, -8   # Reservar espacio para $ra, $fp")
            self.add_code("sw $ra, 0($sp)      # Guardar $ra")
            self.add_code("sw $fp, 4($sp)      # Guardar $fp")
            self.add_code("move $fp, $sp       # Establecer nuevo frame pointer")
            self.add_code(f"addi $sp, $sp, -{self.current_function_max_offset}   # Reservar espacio para variables locales")
        
            return
        
        label = instruction.name
        self.check_ambiguous_region(label) # Chequear si se trata de la label de salida de una región ambigua
        self.add_code(f"{label}:")
        
    def jump(self, instruction):
        
        label = instruction.label
        op = instruction.op
        arg1 = instruction.arg1
        arg2 = instruction.arg2
        
        if instruction.ambiguous:
            self.ambiguous_region = True
            
        else:
            if self.ambiguous_region:
                self.set_ambiguous_region_exit(label)
            
        if arg1 is None:
            self.add_code(f"j {label}")
            return
        
        arg1_reg = self.load_variable(arg1)
        
        
        if op == '>':
            # El arg2 siempre es una variable
            
            arg2_reg = self.load_variable(arg2)
            
            # PARA FLOATS
            # Mover el valor las variables en un registro float
            """ self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
            self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{arg2.name}' en un registro float")
            
            self.add_code("c.lt.s $f2, $f1") # Si es menor que, se debe cambiar el orden de los registros
            self.add_code(f"bc1t {label}") # Saltar si es verdadero, porque $f1 >= $f2 """
            
            # PARA ENTEROS
            # Comparar los valores en los registros
            self.add_code(f"bgt ${arg1_reg}, ${arg2_reg}, {label} # Saltar a {label} si {arg1.name} > {arg2.name}")
            
        elif op == '<':
            # El arg2 siempre es una variable
            
            arg2_reg = self.load_variable(arg2)
            
            # PARA FLOATS
            """ # Mover el valor las variables en un registro float
            self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
            self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{arg2.name}' en un registro float")
            
            self.add_code("c.lt.s $f1, $f2") # Si es menor que
            self.add_code(f"bc1t {label}") # Saltar si es verdadero """
            
            # PARA ENTEROS
            # Comparar los valores en los registros
            self.add_code(f"blt ${arg1_reg}, ${arg2_reg}, {label} # Saltar a {label} si {arg1.name} < {arg2.name}")
            
        elif op is None: # op = '=='
            
            # El arg2 puede ser una variable o una constante
            
            if isinstance(arg2, Symbol):
                
                arg2_reg = self.load_variable(arg2)
                
                # PARA FLOATS
                # Mover el valor las variables en un registro float
                """ self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
                self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{arg2.name}' en un registro float")
                
                self.add_code("c.eq.s $f1, $f2 # Si son iguales saltar") # Si es igual que
                self.add_code(f"bc1t {label}") # Saltar si es verdadero """
                
                # PARA ENTEROS
                # Comparar los valores en los registros
                self.add_code(f"beq ${arg1_reg}, ${arg2_reg}, {label} # Saltar a {label} si {arg1.name} == {arg2.name}")
                
            else:
                    
                    
                    arg2_reg = self.load_constant(arg2)
                    
                    # PARA FLOATS
                    # self.add_code(f"mtc1 ${arg2_reg}, $f2 # Mover el valor de la constante '{arg2}' en un registro float")
                    # Mover el valor la variable a un registro float
                    """ self.add_code(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
                    
                    self.add_code("c.eq.s $f1, $f2") # Si es igual que
                    self.add_code(f"bc1t {label}") # Saltar si es verdadero """
                    
                    # PARA ENTEROS
                    # Comparar los valores en los registros
                    self.add_code(f"beq ${arg1_reg}, ${arg2_reg}, {label} # Saltar a {label} si {arg1.name} == {arg2}")
                    
        return
    
    def call(self, instruction):
            
            label = instruction.label
            arguments = instruction.arguments
            
            self.calling_subroutine = label
            
            arg_number = 0
            for arg in arguments:
                
                if isinstance(arg.type, InstanceType):
                    
                    arg_reg = self.load_variable(arg, instance=True)
                    
                else:
                    arg_reg = self.load_variable(arg)
                
                # Guardar el valor de la variable en el stack
                self.add_code(f"move $a{arg_number}, ${arg_reg} # Guardar el valor de la variable '{arg.name}' en a{arg_number}")
                
                arg_number += 1
                
            # Llamar a la subrutina    
            self.add_code(f"jal {label}")
            self.reset_after_subroutine()
            
    def return_(self, instruction):
        
        if self.return_symbol:
            self.add_code(f"lw $v0, {self.return_symbol.offset + 8}($fp)  # Leer el valor de retorno desde la ultima posicion")
        
        # Epilogo de la función
        
        self.add_code(f"addi $sp, $sp, {self.current_function_max_offset}     # Limpiar espacio de variables locales")
        self.add_code("lw $fp, 4($sp)        # Restaurar $fp")
        self.add_code("lw $ra, 0($sp)        # Restaurar $ra")
        self.add_code("addi $sp, $sp, 8      # Restaurar $sp al estado previo")
        self.add_code("jr $ra                # Retornar al llamador")
        
    def end_function(self, instruction):
        self.in_subroutine = False
        self.subroutine_label = None
        self.current_function_max_offset = 0
        self.a_count = 0
        self.reset_after_subroutine()
        
    def param(self, instruction):
        
        arg = instruction.param
        
        # Guardar el valor de la variable en el stack
        self.add_code(f"sw $a{self.a_count}, {arg.offset + 8}($fp) # Guardar el valor de la variable '{arg.name}' en el stack")
        
        self.a_count += 1
        
    def alloc(self, instruction):
            
        # Obtener la variable a asignar
        dest = instruction.dest
        
        # Verificar si la variable ya tiene una dirección asignada
        self.allocate_memory(dest)
        
        return
    
    def concat(self, instruction):
        arg1 = instruction.arg1
        arg2 = instruction.arg2
        dest = instruction.dest
        
        if dest.scope == 'GP':
            
            # Obtener los registros de las variables de entrada (siempre son temporales)
            arg1_reg = self.load_variable(instruction.arg1, instance=True)
            arg2_reg = self.load_variable(instruction.arg2, instance=True)
        
            # Liberar el registro de arg1 (si no es necesario mantenerlo)
            self.current_instruction_register = None
        
            # Primero verificar si la variable destino ya tiene una dirección asignada
            self.allocate_memory(dest) # Si no está en el descriptor de direcciones, se debe asignar una dirección del heap
            
            # Obtener la dirección de memoria de la variable destino
            address = self.address_descriptor[dest.id].address
            
            # Obtener un registro disponible para cargar la dirección de la variable destino
            dest_reg = self.get_reg(address)
            
            dest_reg = dest_reg['register']
            
            self.add_code(f"lw ${dest_reg}, {address} # La direccion del heap de la variable '{dest.name}' se carga en ${dest_reg}")
            
        else:
            
            # Obtener la dirección del stack de las cadenas
            arg1_reg = self.get_reg(arg1.id)['register']
            arg2_reg = self.get_reg(arg2.id)['register']
            
            # Actualizar el descriptor de registros
            self.register_descriptor[arg1_reg] = arg1.id
            self.register_descriptor[arg2_reg] = arg2.id
            
            self.add_code(f"lw ${arg1_reg}, {arg1.offset + 8}($fp) # La direccion del heap de la variable '{arg1.name}' se carga en ${arg1_reg}")
            self.add_code(f"lw ${arg2_reg}, {arg2.offset + 8}($fp) # La direccion del heap de la variable '{arg2.name}' se carga en ${arg2_reg}")
            
            
            # Reservar espacio en el heap para la variable destino
            # Las cadenas no caben en el stack, se deben almacenar en el heap
                
            # Llamar a subrutina para alojar memoria en el heap y retornar la dirección de memoria asignada
            self.add_code(f"li $s0, 255 # Tamano de la cadena a copiar")
            self.add_code("jal alloc_memory # Reservar espacio en el heap para la cadena")
            
            # Obtener un registro base para cargar la dirección del stack de la variable
            dest_reg = self.get_reg('$fp')['register']
            
            self.add_code(f"addi ${dest_reg}, $fp, {dest.offset + 8} # La direccion del stack de la variable '{dest.name}' se carga en ${dest_reg}")
            
            # Almacenar la dirección de memoria de la cadena en el stack
            self.add_code(f"sw $s1, 0(${dest_reg}) # Almacenar la direccion de memoria de la cadena '{dest.name}' en el stack")
            
            # Cargar la dirección de memoria de la cadena en un registro
            self.add_code(f"lw ${dest_reg}, 0(${dest_reg}) # La direccion de memoria de la cadena '{dest.name}' se carga en ${dest_reg}")
            
            # Actualizar el descriptor de registros
            self.register_descriptor[dest_reg] = f'{dest.name}[{dest.offset + 8}]'
        
        # Realizar la concatenación de strings
        
        # Manejar el primer operando (cadena o número)
        if isinstance(arg1.type, (StringType, AnyType)):
            
            # Copiar caracteres de la cadena al destino
            self.add_code(f"move $s0, ${arg1_reg} # Direccion de la cadena a copiar")
            self.add_code(f"move $s3, ${dest_reg} # Direccion de la cadena destino")
            self.add_code(f"li $s1, 0 # Offset inicial para la copia")
            self.add_code("jal copy_string # Concatenar cadenas")
            
        elif isinstance(arg1.type, NumberType):
            # Convertir el número a cadena y copiar
            self.add_code(f"move $a0, ${arg1_reg} # Numero a convertir")
            self.add_code("li $v0, 1      # Syscall para imprimir enteros (sin imprimir)")
            self.add_code("syscall        # Convertir numero a cadena")
            self.add_code(f"la ${arg1_reg}, ${dest_reg} # Direccion temporal de la cadena")
            self.copy_string(arg1_reg, dest_reg, start_offset=0)
            
        # Manejar el segundo operando (cadena o número)
        if isinstance(arg2.type, (StringType, AnyType)):
            # Copiar caracteres de la cadena al destino
            self.add_code(f"move $s0, ${arg2_reg} # Direccion de la cadena a copiar")
            self.add_code(f"move $s3, ${dest_reg} # Direccion de la cadena destino")
            self.add_code("jal copy_string # Concatenar cadenas")
            
        elif isinstance(arg2.type, NumberType):
            # Convertir el número a cadena y copiar
            self.add_code(f"move $a0, ${arg2_reg} # Numero a convertir")
            self.add_code("li $v0, 1      # Syscall para imprimir enteros (sin imprimir)")
            self.add_code("syscall        # Convertir número a cadena")
            self.add_code(f"la ${arg2_reg}, {dest_reg} # Direccion temporal de la cadena")
            self.copy_string(arg2_reg, dest_reg, start_offset=arg1.type.size)

        if dest.scope == 'GP':
            # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
            self.address_descriptor[instruction.dest.id].registers = [dest_reg]
            self.address_descriptor[instruction.dest.id].address_valid = False
        