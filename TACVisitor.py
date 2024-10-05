from CompiscriptParser import CompiscriptParser
from CompiscriptVisitor import CompiscriptVisitor
from IntermediateCodeGenerator import ThreeAddressInstruction, IntermediateCodeGenerator

class TACVisitor():
    def __init__(self, symbol_table):
        self.result = []
        self.code_generator = IntermediateCodeGenerator()
        self.current_offset = 0
        self.symbol_table = symbol_table
        
    def visitPrimary(self, ctx):
        value = None
        
        if ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
                
        elif ctx.STRING():
            value = ctx.STRING().getText()
        
        elif ctx.IDENTIFIER():
            value = ctx.IDENTIFIER().getText()
            
        return value
            
    def visitCall(self, ctx):
        value = self.visit(ctx.primary())
        return value
        
    def visitUnary(self, ctx):
        # Caso 1: es un operador unario
        if ctx.getChildCount() == 2:  # Esto indica que hay un operador unario seguido por otro unary
            
            operator = ctx.getChild(0).getText()
            
            op = 'NEG' if operator == '-' else 'NOR'
            
            value = self.visit(ctx.unary())
            temp_name = self.code_generator.new_temp()
            
            self.symbol_table.add_temp(temp_name, value)
            
            self.code_generator.add_instruction(op=op, dest=temp_name, arg1=value)
            
            return temp_name
        
        # Caso 2: Visitar a call
        else:
            return self.visit(ctx.call())
        
    def visitFactor(self, ctx):
        return super().visitFactor(ctx)
    
    def visitTerm(self, ctx: CompiscriptParser.TermContext):
        return super().visitTerm(ctx)
    
    
            
            