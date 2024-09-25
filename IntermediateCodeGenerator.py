class ThreeAddressInstruction:
    def __init__(self, op, dest=None, arg1=None, arg2=None, result=None, next=None):
        self.op = op  # Operación, como ADD, SUB, etc.
        self.dest = dest  # Variable o registro de destino
        self.arg1 = arg1  # Primer operando (puede ser None para operaciones unarias)
        self.arg2 = arg2  # Segundo operando (puede ser None si no se usa)
        self.result = result
        self.next = next

    def __str__(self):
        # Representación en formato de tres direcciones
        return f"{self.op} {self.dest}, {self.arg1}, {self.arg2}" if self.arg2 else f"{self.op} {self.dest}, {self.arg1}"
    
class IntermediateCodeGenerator:
    def __init__(self):
        self.instructions = []
        self.temp_count = 0
        self.offset = 0
        
    def add_instruction(self, op, dest=None, arg1=None, arg2=None, result=None):
        instruction = ThreeAddressInstruction(op, dest, arg1, arg2, result)
        self.instructions.append(instruction)
        
    def __str__(self):
        return "\n".join(str(instruction) for instruction in self.instructions)