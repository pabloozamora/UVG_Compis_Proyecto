from IntermediateCodeGenerator import ThreeAddressInstruction, PrintInstruction, Label, JumpInstruction
from SymbolTable import Symbol, TempSymbol, NumberType

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
        self.register_descriptor = {
            't0': None,'t1': None, 't2': None, 't3': None, 't4': None, 't5': None, 't6': None, 't7': None,
        }
        self.address_descriptor = {}
        self.current_instruction_register = None
        self.ambiguous_region = False
        self.ambiguous_region_exit = None
        
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
            
        
    def reset_registers(self):
        
        # Guardar en el heap los valores de los registros que no tienen su último valor válido en memoria
        for name, variable in self.address_descriptor.items():
    
            if not variable.address_valid: # Si la variable no tiene su último valor válido en memoria
                # Cargar la dirección del heap de la variable en un registro
                self.mips_code.append(f"lw $a3, {variable.address} # Guardar variables antes de ambiguedad")
                self.mips_code.append(f"sw ${variable.registers[0]}, {variable.offset}($a3)")
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
        
    def allocate_memory(self, symbol):
        if not self.address_descriptor.get(symbol.id): # Si la variable no está en el descriptor de direcciones, se debe asignar una dirección del heap
            # Pendiente: Determinar si el scope GP o SP
            # GP
            data_address = hex(DATA_BP + symbol.offset) # Calcular la dirección en la sección de data según el offset de la variable
            
            # Si se está dentro de una región ambigua, no se guarda en el descriptor de direcciones, ya que podría ejecutarse o no
            # Por tanto, se debe volver a chequear si la variable ya está en memoria estática
            self.address_descriptor[symbol.id] = AddressDescription(symbol, data_address, ambiguous=self.ambiguous_region) # Guardar la dirección en el descriptor de direcciones
            
            # Saltar a la subrutina para revisar si la variable ya está en memoria estática
            # Preparar los argumentos para la subrutina
            self.mips_code.append(f"li $a1, {data_address} # Cargar la direccion asignada para la variable '{symbol.name}' en memoria estatica")
            self.mips_code.append(f"li $a2, {symbol.type.size} # Cargar los bytes que necesita del heap")
            self.mips_code.append('jal check_existing_variable')
        
        return
        
    def load_constant(self, constant):
        
        # Determinar el tipo de constante
        
        # Si es un número
        if isinstance(constant, float) or isinstance(constant, int):
            constant = float(constant)
            self.mips_code.append(f"li.s $f1, {constant}")
            
            # Obtener un registro disponible para mover el valor del registro float al registro entero
            register = self.get_reg(constant)
            
            # Mover el valor del registro float al registro entero
            self.mips_code.append(f"mfc1 ${register['register']}, $f1")
            
            return register['register']
    
    # Param offset: Si no se envía un offset, únicamente se devuelve la dirección de memoria de la variable
    def load_variable(self, symbol, offset=0):
        
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
            self.mips_code.append(f"lw ${address_reg}, {address} # La direccion del heap de la variable '{symbol.name}' se carga en ${address_reg}")
        
        # Actualizar el descriptor de registros
        self.register_descriptor[address_reg] = address
        
        if offset is None:
            return address_reg
        
        # Obtener un registro disponible para guardar el valor de la variable
        value_reg = self.get_reg(symbol.id)['register']
        
        # Cargar el valor de la dirección del heap en el registro
        self.mips_code.append(f"lw ${value_reg}, {offset}(${address_reg}) # El valor de la variable '{symbol.name}' en el heap se carga en ${value_reg}")
        
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
            self.mips_code.append(f'addi, $sp, $sp, -4 # Reservar espacio en el stack para almacenar el valor de temp_reg')
            self.mips_code.append(f'sw ${temp_reg}, 0($sp) # Guardar el valor de temp_reg en el stack')
            
            # Cargar la dirección del heap de la variable en un registro
            self.mips_code.append(f"lw $t0, {self.address_descriptor[variable_to_replace].address}")
            self.mips_code.append(f"sw {register_to_replace}, {self.address_descriptor[variable_to_replace].offset}(${temp_reg})")
            
            # Recuperar temp_reg del stack
            self.mips_code.append(f'lw ${temp_reg}, 0($sp) # Recuperar el valor de temp_reg del stack')
            self.mips_code.append(f'addi, $sp, $sp, 4 # Liberar espacio en el stack')
            
            # Indicar en el descriptor de direcciones que la variable ya no tiene su último valor válido en el registro, sino en el heap
            self.address_descriptor[variable_to_replace].registers.remove(register_to_replace)
            self.address_descriptor[variable_to_replace].address_valid = True
            
            return {'register': register_to_replace, 'already_loaded': False}
        
        return None
    
    def write_code(self, file_name='output.asm'):
        with open(file_name, 'w') as file:
            
            file.write(".text\n")
            file.write(".globl main\n")
            file.write("main:\n")
            
            for line in self.mips_code:
                file.write(f"{line}\n")
                
            file.write("li $v0, 10\n")
            file.write("syscall\n")
            
            # Subrutina para revisar si la variable ya está en memoria estática
            # s0: Dirección de la variable en memoria estática
            # s1: Tamaño de la variable
            
            file.write('\ncheck_existing_variable:\n')
            file.write('lw $s0, 0($a1) # Cargar la dirección de la variable en memoria estática\n')
            file.write('bnez $s0, end_check_existing_variable # Si la direccion (argumento 1) no es 0, regresar\n')
            file.write('save_variable:\n')
            file.write(f"li $v0, 9\n")
            file.write(f"move $a0, $a2 # Obtener el tamano de la variable del argumento 2\n")
            file.write("syscall\n")
            file.write(f"move $a2, $v0 # Guardar la direccion de memoria asignada en $a2\n")
            file.write("sw $a2, 0($a1) # Guardar la direccion de memoria asignada en la variable en memoria estatica\n")
            file.write('end_check_existing_variable:\n')
            file.write('jr $ra\n')
        
    def generate(self):
        for instruction in self.intermediate_code:
            print('Instruction:', instruction)
            if isinstance(instruction, ThreeAddressInstruction):
                if instruction.op == '=':
                    self.assign(instruction)
                elif instruction.op == 'ADD':
                    self.add(instruction)
                elif instruction.op == 'SUB':
                    self.sub(instruction)
                elif instruction.op == 'MUL':
                    self.mul(instruction)
                elif instruction.op == 'DIV':
                    self.div(instruction)
                elif instruction.op == 'ASSIGN':
                    self.assign(instruction)
                elif instruction.op == 'GOTO':
                    self.goto(instruction)
                elif instruction.op == 'IF':
                    self.if_statement(instruction)
                elif instruction.op == 'LABEL':
                    self.label(instruction)
                elif instruction.op == 'PRINT':
                    self.print(instruction)
                elif instruction.op == 'READ':
                    self.read(instruction)
                    
            elif isinstance(instruction, PrintInstruction):
                self.print(instruction)
                
            elif isinstance(instruction, Label):
                self.label(instruction)
                
            elif isinstance(instruction, JumpInstruction):
                self.jump(instruction)
        
        self.write_code()
        
    def assign(self, instruction):
        dest = instruction.dest
        value = instruction.arg1
            
        # El último valor válido de la variable destino ahora debe apuntar al último valor válido de la variable value
        self.allocate_memory(dest) # Verificar si la variable destino ya tiene una dirección asignada
        
        if value is None: # Si no se trata de una asignación, sino de una declaración de variable, solo se debe reservar la memoria en el heap
            self.current_instruction_register = None
            return
        
        # Verificar si el valor a asignar es una variable o una constante
        if isinstance(value, Symbol):
            
            # Si es una variable, ya está en el descriptor de direcciones, cargar su valor verdadero en un registro
            value_reg = self.load_variable(value)
            
        else:
            
            # Si es una constante, cargar su valor en un registro
            value_reg = self.load_constant(value)
            
        # Almacenar el valor en la dirección del heap de la variable destino
        # self.mips_code.append(f"sw ${value_reg}, 0(${dest_reg})") # Si el valor debe cargarse de un offset de la variable, indicarlo
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[dest.id].registers.append(value_reg) # Último valor válido de la variable destino ahora es el valor de la variable value
        self.address_descriptor[dest.id].address_valid = False
    
    def add(self, instruction):
        
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable arg1 en un registro float")
        self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable arg2 en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("add.s $f3, $f1, $f2")
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.mips_code.append(f"mfc1 ${dest_reg}, $f3")
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = False
    
    def sub(self, instruction):
       # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable arg1 en un registro float")
        self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable arg2 en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("sub.s $f3, $f1, $f2")
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.mips_code.append(f"mfc1 ${dest_reg}, $f3")
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def mul(self, instruction):
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable arg1 en un registro float")
        self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable arg2 en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("mul.s $f3, $f1, $f2")
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.mips_code.append(f"mfc1 ${dest_reg}, $f3")
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def div(self, instruction):
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Mover el valor de las variables a un registro float
        self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable arg1 en un registro float")
        self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable arg2 en un registro float")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("div.s $f3, $f1, $f2")
        
        # Obtener un registro para guardar el resultado de la suma
        dest_reg = self.get_reg(instruction.dest.id)['register']
        self.mips_code.append(f"mfc1 ${dest_reg}, $f3")
        
        # Verificar que ya se tenga una dirección asignada para la variable destino
        self.allocate_memory(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        # self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino ya no tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = False
        
    def print(self, instruction):
        arg = instruction.arg
        
        # Cargar el valor de la variable a imprimir en un registro
        arg_reg = self.load_variable(arg)
        
        # Validar si el tipo de la variable es float
        if isinstance(arg.type, NumberType) and arg.type.is_float:
            # Mover el valor la variable a un registro float
            self.mips_code.append(f"mtc1 ${arg_reg}, $f1")
            
            # Imprimir el valor de la variable
            self.mips_code.append("li $v0, 2")
            self.mips_code.append("mov.s $f12, $f1")
            self.mips_code.append("syscall")
            
    def label(self, instruction):
        label = instruction.name
        self.check_ambiguous_region(label) # Chequear si se trata de la label de salida de una región ambigua
        self.mips_code.append(f"{label}:")
        
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
            self.mips_code.append(f"j {label}")
            return
        
        arg1_reg = self.load_variable(arg1)
        
        
        if op == '>':
            # El arg2 siempre es una variable
            
            arg2_reg = self.load_variable(arg2)
            
            # Mover el valor las variables en un registro float
            self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
            self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{arg2.name}' en un registro float")
            
            self.mips_code.append("c.lt.s $f2, $f1") # Si es menor que, se debe cambiar el orden de los registros
            self.mips_code.append(f"bc1t {label}") # Saltar si es verdadero, porque $f1 >= $f2
            
        elif op == '<':
            # El arg2 siempre es una variable
            
            arg2_reg = self.load_variable(arg2)
            
            # Cargar el valor en el heap de las variables en un registro float
            self.mips_code.append(f"lwc1 $f1, ${arg1_reg}")
            self.mips_code.append(f"lwc1 $f2, ${arg2_reg}")
            
            self.mips_code.append("c.lt.s $f1, $f2") # Si es menor que
            self.mips_code.append(f"bc1f {label}") # Saltar si es verdadero
            
        elif op is None: # op = '=='
            
            # El arg2 puede ser una variable o una constante
            
            if isinstance(arg2, Symbol):
                
                arg2_reg = self.load_variable(arg2)
                
                # Mover el valor las variables en un registro float
                self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
                self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el ultimo valor valido de la variable '{arg2.name}' en un registro float")
                
                self.mips_code.append("c.eq.s $f1, $f2 # Si son iguales saltar") # Si es igual que
                self.mips_code.append(f"bc1t {label}") # Saltar si es verdadero
                
            else:
                    
                    arg2_reg = self.load_constant(arg2)
                    self.mips_code.append(f"mtc1 ${arg2_reg}, $f2 # Mover el valor de la constante '{arg2}' en un registro float")
                    
                    # Mover el valor la variable a un registro float
                    self.mips_code.append(f"mtc1 ${arg1_reg}, $f1 # Mover el ultimo valor valido de la variable '{arg1.name}' en un registro float")
                    
                    self.mips_code.append("c.eq.s $f1, $f2") # Si es igual que
                    self.mips_code.append(f"bc1t {label}") # Saltar si es verdadero
                    
        return
        
        
        