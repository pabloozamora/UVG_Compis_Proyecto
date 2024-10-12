class ThreeAddressInstruction:
    def __init__(self, op, dest=None, arg1=None, arg2=None, next=None):
        self.op = op  # Operación, como ADD, SUB, etc.
        self.dest = dest  # Variable o registro de destino
        self.arg1 = arg1  # Primer operando (puede ser None para operaciones unarias)
        self.arg2 = arg2  # Segundo operando (puede ser None si no se usa)

    def __str__(self):
        # Representación en formato de tres direcciones
        return f"{self.dest} = {self.arg1} {self.op} {self.arg2}" if self.arg2 else f"{self.dest} {self.op} {self.arg1}"
    
class Label:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"{self.name}:"
    
class JumpInstruction:
    def __init__(self, label, arg1=None, arg2=None, op=None):
        self.label = label
        self.arg1 = arg1
        self.arg2 = arg2
        self.op = op
        
    def __str__(self):
        if self.arg1 and self.op:
            return f"if {self.arg1} {self.op} {self.arg2} goto {self.label}"
        elif self.arg1:
            return f"if {self.arg1} == {self.arg2} goto {self.label}"
        return f"goto {self.label}"
    
class ParamInstruction:
    def __init__(self, param):
        self.param = param
        
    def __str__(self):
        return f"param {self.param}"
    
class ReturnInstruction:
    def __init__(self):
        pass
    
    def __str__(self):
        return "return"
    
class CallInstruction:
    def __init__(self, label, arguments):
        self.label = label
        self.arguments = arguments
        
    def __str__(self):
        if self.arguments:
            return f"call {self.label}, {', '.join(str(argument) for argument in self.arguments)}, {len(self.arguments)}"
        return f"call {self.label}"
        
    
class IntermediateCodeGenerator:
    def __init__(self):
        self.instructions = []
        self.label_count = 0
        self.labels = []
        
    def add_instruction(self, op, dest=None, arg1=None, arg2=None, result=None):
        instruction = ThreeAddressInstruction(op, dest, arg1, arg2, result)
        self.instructions.append(instruction)
        
    def add_jump_instruction(self, label, arg1=None, arg2=None, op=None):
        instruction = JumpInstruction(label, arg1, arg2, op)
        self.instructions.append(instruction)
        
    def add_param_instruction(self, param):
        instruction = ParamInstruction(param)
        self.instructions.append(instruction)
        
    def add_return_instruction(self):
        instruction = ReturnInstruction()
        self.instructions.append(instruction)
        
    def add_call_instruction(self, label, arguments):
        instruction = CallInstruction(label, arguments)
        self.instructions.append(instruction)
    
    def new_label(self, name=None):
        if name:
            label = f'L_{name}'
            self.labels.append(label)
            return label
        else:
            self.label_count += 1
            return f"L{self.label_count}"
    
    def add_label(self, label):
        self.instructions.append(Label(label))
        
    def __str__(self):
        return "\n".join(str(instruction) for instruction in self.instructions)