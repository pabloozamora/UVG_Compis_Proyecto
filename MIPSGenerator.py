from IntermediateCodeGenerator import ThreeAddressInstruction, PrintInstruction
from SymbolTable import Symbol, TempSymbol, NumberType

DATA_BP = 0x10000000

class AddressDescription:
    def __init__(self, symbol_id, address=None, offset=0):
        self.symbol_id = symbol_id
        self.registers = []
        self.address = address
        self.address_valid = False
        self.offsett = offset

class MIPSGenerator:
    def __init__(self, intermediate_code):
        self.intermediate_code = intermediate_code
        self.mips_code = []
        self.register_descriptor = {
            't0': None,'t1': None, 't2': None, 't3': None, 't4': None, 't5': None, 't6': None, 't7': None,
        }
        self.address_descriptor = {}
        self.current_instruction_register = None
        
    def load_constant(self, constant):
        
        # Determinar el tipo de constante
        
        # Si es un número
        if isinstance(constant, float):
            self.mips_code.append(f"li.s $f1, {constant}")
            
            # Obtener un registro disponible para mover el valor del registro float al registro entero
            register = self.get_reg(constant)
            
            # Mover el valor del registro float al registro entero
            self.mips_code.append(f"mfc1 ${register['register']}, $f1")
            
            return register['register']
    
    # Param offset: Si se desea acceder a un desplazamiento específico de la variable
    def load_variable(self, symbol, offset=None):
        
        # Primero verificar si la variable destino ya tiene una dirección asignada
        
        if not self.address_descriptor.get(symbol.id): # Si no está en el descriptor de direcciones, se debe asignar una dirección del heap
            
            # Pendiente: Determinar si el scope GP o SP
            
            # GP
            data_address = hex(DATA_BP + symbol.offset) # Calcular la dirección en la sección de data según el offset de la variable
            self.address_descriptor[symbol.id] = AddressDescription(symbol.id, data_address) # Guardar la dirección en el descriptor de direcciones
            
            # Reservar memoria en el heap
            self.mips_code.append(f"li $v0, 9")
            self.mips_code.append(f"li $a0, {symbol.type.size}")
            self.mips_code.append("syscall")
            self.mips_code.append(f"sw $v0, {data_address}")
        
        # Obtener la dirección de memoria de la variable
        address = self.address_descriptor[symbol.id].address
        
        # Obtener un registro disponible para cargar la dirección de la variable
        register = self.get_reg(address)
        
        address_reg = register['register']
        address_already_loaded = register['already_loaded']
        
        if not address_already_loaded: # Si la dirección de la variable no estaba en un registro, se debe cargar en un registro
        
            # Cargar la dirección del de la variable en el registro
            self.mips_code.append(f"lw ${address_reg}, {address}")
        
        # Actualizar el descriptor de registros
        self.register_descriptor[address_reg] = symbol.id
        
        if offset is None:
            return address_reg
        
        # Obtener un registro disponible para guardar el valor de la variable
        variable_reg = self.get_reg(symbol.id)['register']
        
        # Cargar el valor de la dirección del heap en el registro
        self.mips_code.append(f"lw ${variable_reg}, {offset}(${address_reg})")
        
        # Actualizar el descriptor de registros
        self.register_descriptor[variable_reg] = symbol.id
        
        return variable_reg
        
    def get_reg(self, symbol_id):
    
        # Arreglo de registros disponibles
        available_registers = []
        
        # Primero, se verifica si la variable ya está en un registro
        
        for reg, value in self.register_descriptor.items():
            
            if value is symbol_id:
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
            self.mips_code.append(f"sw {register_to_replace}, {self.address_descriptor[variable_to_replace].offset}({self.address_descriptor[variable_to_replace].address})")
            
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
        
        self.write_code()
        
    def assign(self, instruction):
        dest = instruction.dest
        value = instruction.arg1
            
        # Cargar la dirección del heap de la variable destino en un registro
        dest_reg = self.load_variable(dest) # Si el valor debe asignarse a un offset de la variable destino, indicarlo
        
        if value is None:
            return
        
        # Verificar si el valor a asignar es una variable o una constante
        if isinstance(value, Symbol):
            
            # Si es una variable, cargar su dirección del heap en un registro
            value_reg = self.load_variable(value)
            
            # Cargar el valor en el heap de la variable en un registro
            self.mips_code.append(f"lw ${value_reg}, 0(${value_reg})") # Si el valor debe cargarse de un offset de la variable, indicarlo
            
        else:
            
            # Si es una constante, cargar su valor en un registro
            value_reg = self.load_constant(value)
            
        # Almacenar el valor en la dirección del heap de la variable destino
        self.mips_code.append(f"sw ${value_reg}, 0(${dest_reg})") # Si el valor debe cargarse de un offset de la variable, indicarlo
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino tiene su último valor válido en memoria
        self.address_descriptor[dest.id].registers.append(dest_reg)
        self.address_descriptor[dest.id].address_valid = True
    
    def add(self, instruction):
        
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        
        # Reservar el registro de arg1 para la instrucción actual
        self.current_instruction_register = arg1_reg
        
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Cargar el valor en el heap de las variables en un registro float
        self.mips_code.append(f"lwc1 $f1, 0(${arg1_reg})")
        self.mips_code.append(f"lwc1 $f2, 0(${arg2_reg})")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("add.s $f3, $f1, $f2")
        
        dest_reg = self.load_variable(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = True
    
    def sub(self, instruction):
       # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        
        # Reservar el registro de arg1 para la instrucción actual
        self.current_instruction_register = arg1_reg
        
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Cargar el valor en el heap de las variables en un registro float
        self.mips_code.append(f"lwc1 $f1, 0(${arg1_reg})")
        self.mips_code.append(f"lwc1 $f2, 0(${arg2_reg})")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("sub.s $f3, $f1, $f2")
        
        dest_reg = self.load_variable(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = True
        
    def mul(self, instruction):
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        
        # Reservar el registro de arg1 para la instrucción actual
        self.current_instruction_register = arg1_reg
        
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Cargar el valor en el heap de las variables en un registro float
        self.mips_code.append(f"lwc1 $f1, 0(${arg1_reg})")
        self.mips_code.append(f"lwc1 $f2, 0(${arg2_reg})")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("mul.s $f3, $f1, $f2")
        
        dest_reg = self.load_variable(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = True
        
    def div(self, instruction):
        # arg1 y arg2 siempre son variables (la suma siempre involucra temporales)
        arg1_reg = self.load_variable(instruction.arg1)
        
        # Reservar el registro de arg1 para la instrucción actual
        self.current_instruction_register = arg1_reg
        
        arg2_reg = self.load_variable(instruction.arg2)
        
        # Cargar el valor en el heap de las variables en un registro float
        self.mips_code.append(f"lwc1 $f1, 0(${arg1_reg})")
        self.mips_code.append(f"lwc1 $f2, 0(${arg2_reg})")
        
        # Liberar el registro de arg1
        self.current_instruction_register = None
        
        # Hacer la operación de floats
        self.mips_code.append("div.s $f3, $f1, $f2")
        
        dest_reg = self.load_variable(instruction.dest)
        
        # Almacenar el resultado en el registro de la variable destino
        self.mips_code.append(f"swc1 $f3, 0(${dest_reg})")
        
        # Actualizar el descriptor de direcciones para indicar que la variable destino tiene su último valor válido en memoria
        self.address_descriptor[instruction.dest.id].registers.append(dest_reg)
        self.address_descriptor[instruction.dest.id].address_valid = True
        
    def print(self, instruction):
        arg = instruction.arg
        
        # Cargar la dirección del heap de la variable a imprimir en un registro
        arg_reg = self.load_variable(arg)
        
        # Validar si el tipo de la variable es float
        if isinstance(arg.type, NumberType) and arg.type.is_float:
            # Cargar el valor en el heap de la variable en un registro float
            self.mips_code.append(f"lwc1 $f1, 0(${arg_reg})")
            
            # Imprimir el valor de la variable
            self.mips_code.append("li $v0, 2")
            self.mips_code.append("mov.s $f12, $f1")
            self.mips_code.append("syscall")