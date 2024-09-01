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
        self.return_types = set()
    
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
        
        # Visitar la definición de función y obtener el nombre y tipo de la función
        function_name, function_type = self.visitChildren(ctx)
        
        symbol = None
        
        # IMPORTANTE: Esto podría cambiarse por sustituir la función en la tabla de símbolos
        
        # Verificar si la función ya ha sido declarada
        declared_function = self.symbol_table.lookup(function_name)
        if declared_function and declared_function.type.arg_types == function_type.arg_types:
            print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la función {function_name} con parámetros {function_type.arg_types} ya ha sido declarada")
        else:
            # Crear un símbolo para la función
            symbol = self.symbol_table.add(function_name, function_type)
        
        return symbol


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
            var_value, var_type, _ = self.visit(ctx.expression())
            
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
        print("Visita al nodo de retorno")

        # Obtener la expresión de retorno si existe
        if ctx.expression():
            return_value, return_type, return_name = self.visit(ctx.expression())
            print(f"Tipo de retorno encontrado: {return_type}")
            self.return_types.add(return_type)
        else:
            # Si no hay expresión, es un retorno implícito de 'nil'
            self.return_types.add(NilType())
            print("Retorno implícito de 'nil'")
            
        return self.return_types


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
        var_name = None
        var_value = None
        var_type = NilType()
        
        var_value, var_type, var_name = self.visitChildren(ctx)
        
        print('Asignación: Hijo obtenido: ', var_value)
        
        var_name_node = ctx.IDENTIFIER()  # Intenta obtener el nodo del identificador
        
        print('Asignación: Nombre variable: ', var_name_node)
    
        if var_name_node is not None: # (Se está repitiendo la asignación)
            
            var_name = var_name_node.getText()
            
            # Buscar la variable en la tabla de símbolos
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol is None: # La variable no ha sido declarada
                print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} no ha sido declarada")
                
            else:
                
                # Determinar el tipo del valor que está siendo asignado
                symbol.type = var_type
                symbol.value = var_value
                print(f"Variable {var_name} de tipo {var_type} asignada con valor {var_value}")
            
        return var_value, var_type, var_name


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
        print("Visita al nodo de llamada a función")

        # Obtener el nombre de la función llamada
        value, type, name = self.visit(ctx.primary())
        
        print(ctx.getText())
        
        # Si primary_result[1] es None, o no hay () en el texto, significa que no se trata de una función
        if '(' not in ctx.getText():
            return value, type, name
        
        if not isinstance(type, FunctionType):
            print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: '{name}' no es una función.")
            return None, None, None
        
        # Buscar la función en la tabla de símbolos
        function_symbol = self.symbol_table.lookup(name)

        if not function_symbol:
            print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: La función '{name}' no ha sido declarada.")
            return None, None, None

        # Validar los argumentos pasados a la función
        arguments = []
        if ctx.arguments():
            for arg in ctx.arguments():
                arguments = self.visit(arg)

        if len(arguments) != len(function_symbol.type.arg_types):
            print(f"Error semántico: La función '{name}' espera {len(function_symbol.type.arg_types)} argumentos, pero se pasaron {len(arguments)}.")
            return None, None, None

        return None, function_symbol.type.return_type, name


    # Visit a parse tree produced by CompiscriptParser#primary.
    def visitPrimary(self, ctx:CompiscriptParser.PrimaryContext):
        print('Visita al nodo de primary')
        # result = self.visitChildren(ctx)
        value = None
        type = NilType()
        var_name = None
        
        if ctx.NUMBER() or ctx.STRING(): # Si es número o cadena
            
            if ctx.NUMBER():
                value = float(ctx.NUMBER().getText())
                type = NumberType()
                
            elif ctx.STRING():
                value = ctx.STRING().getText()
                type = StringType()
                
            elif ctx.getText() == 'nil':
                value = None
                type = NilType()
            
            elif ctx.getText() == 'true':
                value = True
                type = BooleanType()
                
            elif ctx.getText() == 'false':
                value = False
                type = BooleanType()
                
        elif ctx.IDENTIFIER(): # Si es un identificador
            var_name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol:
                value = symbol.value
                type = symbol.type
                print(f"{var_name} encontrada con tipo {type} y valor {value}")
                
            else:
                print(f'Error semántico línea {ctx.start.line}, posición {ctx.start.column}: "{var_name}" no ha sido declarada')
        
        return value, type, var_name
            

    # Visit a parse tree produced by CompiscriptParser#function.
    def visitFunction(self, ctx:CompiscriptParser.FunctionContext):
        print('Visita al nodo de función')
        
        function_name = ctx.IDENTIFIER().getText()
            
        # El tipo de retorno de la función es 'nil' por defecto.
        return_type = NilType()
        
        # Crear un nuevo ámbito para los parámetros de la función y la función misma (para recursividad)
        self.symbol_table.enter_scope()
        
        # Obtener los parámetros de la función
        parameters = []
        if ctx.parameters():
            parameters = self.visit(ctx.parameters())
        
        # Crear un símbolo para la función
        function_type = FunctionType(return_type, parameters)
        self.symbol_table.add(function_name, function_type)
            
        # Visitar el bloque de la función
        self.visit(ctx.block())
        
        # Salir del ámbito de los parámetros
        self.symbol_table.exit_scope()
        
        # Determinar si la función tiene uno o más valores de retorno
        if self.return_types:
            function_type.return_type = self.return_types
            print(f"Tipos de retorno de la función {function_name}: {function_type.return_type}")
            
        # Limpiar la lista de tipos de retorno para esta función
        self.return_types = set()
        
        return function_name, function_type


    # Visit a parse tree produced by CompiscriptParser#parameters.
    def visitParameters(self, ctx:CompiscriptParser.ParametersContext):
        parameters = []
    
        # Iterar sobre cada IDENTIFIER en el contexto
        for i in range(len(ctx.IDENTIFIER())):
            param_name = ctx.IDENTIFIER(i).getText()
            print(f"Parámetro encontrado: {param_name}")
            
            if self.symbol_table.lookup(param_name):
                print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el parámetro {param_name} ya ha sido declarado en este ámbito")
            else:
                parameters.append(NilType())
                print(f"Parámetro encontrado: {param_name}")
                self.symbol_table.add(param_name, NilType())
            
            # Agregarlo a la tabla de símbolos con tipo 'nil'
            self.symbol_table.add(param_name, NilType())
            
        return parameters


    # Visit a parse tree produced by CompiscriptParser#arguments.
    def visitArguments(self, ctx:CompiscriptParser.ArgumentsContext):
        print("Visita al nodo de argumentos")
        arguments = []
        
        # Iterar sobre cada expression en el contexto
        for i in range(len(ctx.expression())):
            argument = self.visit(ctx.expression(i))
            print('Argumento: ', argument)
            arguments.append(argument)
            print(f"Argumento encontrado: {argument}")
            
        print('Terminando la visita al nodo de argumentos')
            
        return arguments
