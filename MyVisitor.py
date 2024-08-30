from CompiscriptParser import CompiscriptParser
from CompiscriptVisitor import CompiscriptVisitor
from SymbolTable import ListSymbolTable, NumberType, FunctionType, NilType, StringType, BooleanType

def determine_type(value):
        if isinstance(value, int) or isinstance(value, float):
            return NumberType()
        
        elif isinstance(value, bool):
            return BooleanType()
        
        elif isinstance(value, str):
            return StringType()
        
        elif value is None:
            return NilType()

class MyVisitor(CompiscriptVisitor):
    def __init__(self):
        self.symbol_table = ListSymbolTable()
    
    def visitProgram(self, ctx:CompiscriptParser.ProgramContext):
        print('Visita al nodo de inicio del programa')
        self.symbol_table.enter_scope()
        result = self.visitChildren(ctx)
        print('Terminando la visita al nodo de inicio del programa')
        return result
    
    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        print('Visita al nodo de declaración')
        result = self.visitChildren(ctx)
        print('Terminando la visita al nodo de declaración')
        return result

    # Visit a parse tree produced by CompiscriptParser#classDecl.
    def visitClassDecl(self, ctx:CompiscriptParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#funDecl.
    def visitFunDecl(self, ctx:CompiscriptParser.FunDeclContext):
        print('Visita al nodo de declaración de función')
        
        # Aquí no se hace nada, hay que visitar "function"
        # Visitar la definición de función
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#varDecl.
    def visitVarDecl(self, ctx:CompiscriptParser.VarDeclContext):
        print('Visita al nodo de declaración de variable')
        
        # Obtener nombre de la variable
        var_name = ctx.IDENTIFIER().getText()
        
        # Verificar si la variable no ha sido declarada
        if (var_name in self.symbol_table.current_scope().symbols):
            print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} ya ha sido declarada")
        
        else:
            
            # Obtener los hijos de 'expression' para determinar el tipo de la variable y su valor
            var_type = NilType()
            var_value = None
            
            expression_value = self.visit(ctx.expression())
            
            if expression_value is not None:
                var_type = determine_type(expression_value)
                var_value = expression_value
            
            # Crear un símbolo para la variable
            symbol = self.symbol_table.add(var_name, var_type, var_value)
            print(f"Variable {var_name} de tipo {var_type} y valor {var_value} declarada")
        
        return var_type


    # Visit a parse tree produced by CompiscriptParser#statement.
    def visitStatement(self, ctx:CompiscriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#exprStmt.
    def visitExprStmt(self, ctx:CompiscriptParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#forStmt.
    def visitForStmt(self, ctx:CompiscriptParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#ifStmt.
    def visitIfStmt(self, ctx:CompiscriptParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#printStmt.
    def visitPrintStmt(self, ctx:CompiscriptParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiscriptParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiscriptParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#block.
    def visitBlock(self, ctx:CompiscriptParser.BlockContext):
        self.symbol_table.enter_scope()
        result = self.visitChildren(ctx)
        self.symbol_table.exit_scope()
        return result


    # Visit a parse tree produced by CompiscriptParser#expression.
    def visitExpression(self, ctx:CompiscriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#assignment.
    def visitAssignment(self, ctx:CompiscriptParser.AssignmentContext):
        print('Visita al nodo de asignación')
        
        assignment_value = self.visitChildren(ctx)
        
        print('Asignación: Hijo obtenido: ', assignment_value)
        
        var_name_node = ctx.IDENTIFIER()  # Intenta obtener el nodo del identificador
        
        print('Asignación: Nombre variable: ', var_name_node)
    
        if var_name_node is not None: # Asignación y no declaración
            
            var_name = var_name_node.getText()
            
            # Buscar la variable en la tabla de símbolos
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol is None: # La variable no ha sido declarada
                print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} no ha sido declarada")
                
            else:
                
                # Determinar el tipo del valor que está siendo asignado
                value_type = determine_type(assignment_value)
                symbol.type = value_type
                symbol.value = assignment_value
                print(f"Variable {var_name} de tipo {value_type} asignada con valor {assignment_value}")
            
        return assignment_value


    # Visit a parse tree produced by CompiscriptParser#logic_or.
    def visitLogic_or(self, ctx:CompiscriptParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#logic_and.
    def visitLogic_and(self, ctx:CompiscriptParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#equality.
    def visitEquality(self, ctx:CompiscriptParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#comparison.
    def visitComparison(self, ctx:CompiscriptParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#term.
    def visitTerm(self, ctx:CompiscriptParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#factor.
    def visitFactor(self, ctx:CompiscriptParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#unary.
    def visitUnary(self, ctx:CompiscriptParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#call.
    def visitCall(self, ctx:CompiscriptParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#primary.
    def visitPrimary(self, ctx:CompiscriptParser.PrimaryContext):
        print('Visita al nodo de primary')
        # result = self.visitChildren(ctx)
        
        if ctx.NUMBER() or ctx.STRING(): # Si es número o cadena
            value = None
            
            if ctx.NUMBER():
                value = float(ctx.NUMBER().getText())
                print(value)
                
            elif ctx.STRING():
                value = ctx.STRING().getText()
                
            elif ctx.getText() == 'nil' or ctx.getText() == 'true' or ctx.getText() == 'false':
                value = ctx.getText()
                
            return value
                
        elif ctx.IDENTIFIER(): # Si es un identificador
            var_name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol:
                value = symbol.value
                print(f"Variable {var_name} encontrada con valor {value}")
                
            else:
                print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} no ha sido declarada")
                return None
            
            return value
            

    # Visit a parse tree produced by CompiscriptParser#function.
    def visitFunction(self, ctx:CompiscriptParser.FunctionContext):
        print('Visita al nodo de función')
        
        function_name = ctx.IDENTIFIER().getText()
        
        # Obtener los parámetros de la función
        
        parameters = []
        if ctx.parameters():
            parameters = self.visit(ctx.parameters())
            
        # Pendiente: Obtener el tipo de retorno de la función
        return_type = NilType()
        
        # Crear un símbolo para la función
        function_type = FunctionType(return_type, parameters)
        self.symbol_table.add(function_name, function_type)
        
        # Crear un nuevo ámbito para los parámetros de la función
        self.symbol_table.enter_scope()
        
        # Agregar los parámetros a la tabla de símbolos
        if parameters:
            for parameter in parameters:
                self.symbol_table.add(parameter, NilType())
            
        # Visitar el bloque de la función
        self.visit(ctx.block())
        
        # Salir del ámbito de los parámetros
        self.symbol_table.exit_scope()
        
        return function_type


    # Visit a parse tree produced by CompiscriptParser#parameters.
    def visitParameters(self, ctx:CompiscriptParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#arguments.
    def visitArguments(self, ctx:CompiscriptParser.ArgumentsContext):
        return self.visitChildren(ctx)
