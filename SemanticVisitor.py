from CompiscriptParser import CompiscriptParser
from CompiscriptVisitor import CompiscriptVisitor
from SymbolTable import ListSymbolTable, NumberType, FunctionType, NilType, StringType, BooleanType, ClassType, InstanceType, AnonymousFunctionType, AnyType
from IntermediateCodeGenerator import IntermediateCodeGenerator
        
def normalize_type(type_obj):
    if not isinstance(type_obj, set):
        return {type_obj}
    return type_obj

def types_are_compatible(left_types, right_types):
    # Normalizar los conjuntos de tipos
    normalized_left_types = normalize_type(left_types)
    normalized_right_types = normalize_type(right_types)
    
    # Comprobar si los tipos en ambos conjuntos son compatibles
    for left_type in normalized_left_types:
        if isinstance(left_type, AnyType):
            return True
        for right_type in normalized_right_types:
            if isinstance(right_type, AnyType):
                return True
            if isinstance(left_type, type(right_type)) or isinstance(right_type, type(left_type)):
                return True
    return False

def types_are_numeric(left_types, right_types):
    # Normalizar los conjuntos de tipos
    normalized_left_types = normalize_type(left_types)
    normalized_right_types = normalize_type(right_types)
    
    # Comprobar si al menos uno de los tipos en ambos conjuntos es numérico o Any
    for left_type in normalized_left_types:
        for right_type in normalized_right_types:
            if (isinstance(left_type, NumberType) or isinstance(left_type, AnyType)) and (isinstance(right_type, NumberType) or isinstance(right_type, AnyType)):
                return True
    return False

def types_are_string(left_types, right_types):
    # Normalizar los conjuntos de tipos
    normalized_left_types = normalize_type(left_types)
    normalized_right_types = normalize_type(right_types)
    #print('left types: ', normalized_left_types)
    #print('right types: ', normalized_right_types)
    
    # Comprobar si al menos uno de los tipos en ambos conjuntos es string o Any
    for left_type in normalized_left_types:
        for right_type in normalized_right_types:
            if (isinstance(left_type, StringType) or isinstance(left_type, AnyType)) and (isinstance(right_type, StringType) or isinstance(right_type, AnyType)):
                return True
    return False

def types_are_boolean(left_types, right_types):
    # Normalizar los conjuntos de tipos
    normalized_left_types = normalize_type(left_types)
    normalized_right_types = normalize_type(right_types)
    
    # Comprobar si al menos uno de los tipos en ambos conjuntos es booleano o Any
    for left_type in normalized_left_types:
        for right_type in normalized_right_types:
            if (isinstance(left_type, BooleanType) or isinstance(left_type, AnyType)) and (isinstance(right_type, BooleanType) or isinstance(right_type, AnyType)):
                return True
    return False

class SemanticVisitor(CompiscriptVisitor):
    def __init__(self):
        self.symbol_table = ListSymbolTable()
        self.return_types = set()
        self.result = []
        self.hasErrors = False
        self.code_generator = IntermediateCodeGenerator()
        self.loop_labels = []
        self.loop_labels_false = []
        
    def getResult(self):
        return self.result
    
    def visitProgram(self, ctx:CompiscriptParser.ProgramContext):
        #print('\n---INICIA EJECUCIÓN---\n')
        result = self.visitChildren(ctx)
        #print('Terminando la visita al nodo de inicio del programa')
        return result
    
    def visitDeclaration(self, ctx: CompiscriptParser.DeclarationContext):
        #print('Visita al nodo de declaración')
        result = self.visitChildren(ctx)
        #print('Terminando la visita al nodo de declaración')
        return result

    # Visit a parse tree produced by CompiscriptParser#classDecl.
    def visitClassDecl(self, ctx:CompiscriptParser.ClassDeclContext):
        #print('Visita al nodo de declaración de clase')
        class_name = ctx.IDENTIFIER(0).getText()
        superclass = None
        
        # Si hay una superclase, resolverla
        if ctx.IDENTIFIER(1):
            superclass_name = ctx.IDENTIFIER(1).getText()
            #print('Supeclase encontrada: ', superclass_name)
            superclass = self.symbol_table.lookup(superclass_name)
            
            if not superclass:
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la superclase {superclass_name} no ha sido declarada")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la superclase {superclass_name} no ha sido declarada")
                self.hasErrors = True
            
            elif not isinstance(superclass.type, ClassType):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: {superclass_name} no es una clase")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: {superclass_name} no es una clase")
                self.hasErrors = True
                superclass = None
                
        # Crear un nuevo ámbito para la clase
        self.symbol_table.enter_scope()
        
        # Crear el tipo de la clase
        class_type = ClassType(class_name, superclass.type if superclass else None)
        
        # Agregar la clase a la tabla de símbolos (Esto solo para que se pueda hacer referencia a la clase dentro de la misma)
        # Posteriormente, se actualizará con los métodos y atributos de la clase
        
        self.symbol_table.add('this', class_type)
        
        # Agregar métodos a la clase
        for method in ctx.function():
            method_name, method_type = self.visit(method)
            class_type.add_method(method_name, method_type)
            
        # Los hijos pudieron haber agregado campos a la clase, por lo que se obtiene nuevamente de la tabla de símbolos
        updated_class = self.symbol_table.lookup('this')
        
        # Eliminar el símbolo this de la tabla de símbolos
        self.symbol_table.delete('this')
        
        # Agregar campos a la clase
        class_type.fields = updated_class.type.fields
        
        # Salir del ámbito de la clase
        self.symbol_table.exit_scope()
        
        # Verificar si la clase ya ha sido declarada
        declared_class = self.symbol_table.lookup(class_name)
        
        if declared_class:
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador {class_name} ya ha sido declarado")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador {class_name} ya ha sido declarado")
            self.hasErrors = True
            return None, None
        
        # Agregar la clase actualizada a la tabla de símbolos
        self.symbol_table.add(class_name, class_type)
        
        #print(f"\nClase {class_name} con superclase {superclass.type if superclass else None} y tipo {class_type} declarada\n")
        
        return class_name, class_type


    # Visit a parse tree produced by CompiscriptParser#funDecl.
    def visitFunDecl(self, ctx:CompiscriptParser.FunDeclContext):
        #print('Visita al nodo de declaración de función')
        
        # Visitar la definición de función y obtener el nombre y tipo de la función
        function_name, function_type = self.visitChildren(ctx)
        
        symbol = None
        
        # IMPORTANTE: Esto podría cambiarse por sustituir la función en la tabla de símbolos
        
        # Verificar si la función ya ha sido declarada
        declared_function = self.symbol_table.lookup(function_name)
        
        if declared_function and not isinstance(declared_function.type, FunctionType):
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: {function_name} ya ha sido declarado como una variable")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: {function_name} ya ha sido declarado como una variable")
            self.hasErrors = True
        
        elif declared_function and len(declared_function.type.arg_types) == len(function_type.arg_types):
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la función {function_name} con parámetros {function_type.arg_types} ya ha sido declarada")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la función {function_name} con parámetros {function_type.arg_types} ya ha sido declarada")
            self.hasErrors = True
            
        else:
            # Crear un símbolo para la función
            symbol = self.symbol_table.add(function_name, function_type)
            
            #print(f"\nFunción {function_name} con parámetros {function_type.arg_types} y tipo de retorno {function_type.return_type} declarada\n")
            
            current_class = self.symbol_table.lookup('this')
            if current_class:
                current_class.add_method(function_name, function_type)
        
        return symbol


    # Visit a parse tree produced by CompiscriptParser#varDecl.
    def visitVarDecl(self, ctx:CompiscriptParser.VarDeclContext):
        #print('Visita al nodo de declaración de variable')
        
        # Obtener nombre de la variable
        var_name = ctx.IDENTIFIER().getText()
        
        # Verificar si la variable no ha sido declarada
        if (var_name in self.symbol_table.current_scope().symbols):
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador '{var_name}' ya ha sido declarado")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador '{var_name}' ya ha sido declarado")
            self.hasErrors = True
            
            return None
        
        else:
            
            var_value = None
            var_type = AnyType()  # Asignar el tipo por defecto a Any
            
            # Si hay una expresión de inicialización, determinar el tipo de la variable y su valor
            if ctx.expression():
                var_value, var_type, _ = self.visit(ctx.expression())
            
            # Crear un símbolo para la variable
            if var_type is not None:
                symbol = self.symbol_table.add(var_name, var_type, value=var_value)
                #print(f"\nVariable {var_name} de tipo {var_type} y valor {var_value} declarada\n")
                
                # Código intermedio
                
                if not self.hasErrors:
                    self.code_generator.add_instruction(op='=', dest=symbol, arg1=var_value)
                
            
        
        return var_type


    # Visit a parse tree produced by CompiscriptParser#statement.
    def visitStatement(self, ctx:CompiscriptParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#exprStmt.
    def visitExprStmt(self, ctx:CompiscriptParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#forStmt.
    def visitForStmt(self, ctx:CompiscriptParser.ForStmtContext):
        #print('Visita al nodo de for')
        
        # Crear un nuevo ámbito para el ciclo for
        self.symbol_table.enter_scope()
        
        # Agregar un símbolo únicamente como indicador si un "break" o "continue" es adecuado
        self.symbol_table.add('for', AnyType())
        
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            self.visit(ctx.exprStmt())
            
        # Los índices de los hijos importantes en `for`:
        cond_index = 3
        update_index = 5
        
        # Código intermedio
        if not self.hasErrors:
            
            # Label para el inicio del bucle
            loop_label = self.code_generator.new_label()
            
            # Agregar la etiqueta de entrada del ciclo a la lista de ciclos
            self.loop_labels.append(loop_label)
            
            # Agregar label de inicio del bucle
            self.code_generator.add_label(loop_label)
            

        # Verificar si hay una expresión condicional en el medio 
        
        if ctx.getChild(cond_index).getText() != ';':  # Si no es un punto y coma, es una expresión
            
            if (ctx.expression(0)): # Verificar que no haya error sintáctico
                cond_value, cond_type, _ = self.visit(ctx.expression(0))
                
                # Verificar si la condición es booleana
                if not any(isinstance(t, BooleanType) for t in normalize_type(cond_type)):
                    #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la condición del bucle 'for' debe ser de tipo booleano")
                    self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la condición del bucle 'for' debe ser de tipo booleano")
                    self.hasErrors = True
                    
                # Código intermedio
                
                if not self.hasErrors:
                        
                        # Label para cuando la condición es falsa
                        false_label = self.code_generator.new_label()
                        
                        # Agregar la etiqueta de salida del ciclo a la lista de ciclos
                        self.loop_labels_false.append(false_label)
                        
                        # Agregar salto para el if de MIPS
                        # Si la condición es falsa, saltar a la etiqueta false_label
                        self.code_generator.add_jump_instruction(false_label, arg1=cond_value, arg2=0)
            
        else :
            
            #print("No hay expresión condicional en el bucle 'for'. Ejecutará hasta un 'break' o 'return'.")
            update_index = 4  # Si no hay condición, el índice de actualización cambia
            
             # Código intermedio
                
            if not self.hasErrors:
                    
                    # Label para cuando la condición es falsa
                    false_label = self.code_generator.new_label()
                    
                    # Agregar la etiqueta de salida del ciclo a la lista de ciclos
                    self.loop_labels_false.append(false_label)
            
        # Visitar la expresión final (si existe y no hay error sintáctico)
        if ctx.getChild(update_index):
            if ctx.getChild(update_index).getText() != ')': # Hay expresión de actualización
                
                update_expression = ctx.getChild(update_index)
                self.visit(update_expression)

        # Visitar el cuerpo del bucle (si no hay error sintáctico)
        if ctx.statement():
            self.visit(ctx.statement())
            
            # Código intermedio
            if not self.hasErrors:
                    
                    # Agregar salto para regresar al inicio del bucle
                    self.code_generator.add_jump_instruction(loop_label)
                    
                    # Agregar label falso para cuando la condición es falsa
                    self.code_generator.add_label(false_label)
                    print('false label: ', false_label)
        
                    # Quitar la etiqueta de salida del ciclo actual
                    self.loop_labels_false.pop()
                    
                    # Quitar la etiqueta de entrada del ciclo actual
                    self.loop_labels.pop()
        
        # Salir del ámbito del ciclo for
        self.symbol_table.exit_scope()

        return None


    # Visit a parse tree produced by CompiscriptParser#ifStmt.
    def visitIfStmt(self, ctx:CompiscriptParser.IfStmtContext):
        #print('Visita al nodo de if')
        
        # Evaluar la condición de B
        condition_value, condition_type, _ = self.visit(ctx.expression())
        
        # Verificar que la condición sea de tipo booleano
        if not any(isinstance(t, BooleanType) for t in normalize_type(condition_type)):
            #print(f"Advertencia línea {ctx.start.line}, posición {ctx.start.column}: la condición del if debe ser de tipo booleano")
            self.result.append(f"Advertencia línea {ctx.start.line}, posición {ctx.start.column}: la condición del if debe ser de tipo booleano")
        
        # Código intermedio
        
        if not self.hasErrors:
                
                # Label para cuando la condición es verdadera
                true_label = self.code_generator.new_label()
                
                # Label para cuando la condición es falsa
                false_label = self.code_generator.new_label()
                
                # Agregar salto para el if de MIPS
                # Si la condición es falsa, saltar a la etiqueta false_label
                self.code_generator.add_jump_instruction(false_label, arg1=condition_value, arg2=0)
        
        # Visitar bloque de código (solo cuando no hay error sintáctico)
        
        if ctx.statement(0):
            self.visit(ctx.statement(0))
            
            # Código intermedio
            # Agregar salto para el final del if
            if not self.hasErrors:
                self.code_generator.add_jump_instruction(true_label)
            
        if ctx.statement(1):  # Existe una cláusula else
            
            # Código intermedio	
            if not self.hasErrors:
                
                # Agregar label falso cuando hay un else
                
                self.code_generator.add_label(false_label)
                
            self.visit(ctx.statement(1))
            
        else:
            # Código intermedio
            if not self.hasErrors:
                self.code_generator.add_label(false_label)
            
        # Código intermedio
        if not self.hasErrors:
            self.code_generator.add_label(true_label)
        
        return None


    # Visit a parse tree produced by CompiscriptParser#printStmt.
    def visitPrintStmt(self, ctx:CompiscriptParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiscriptParser.ReturnStmtContext):
        #print("Visita al nodo de retorno")

        # Obtener la expresión de retorno si existe
        if ctx.expression():
            return_value, return_type, return_name = self.visit(ctx.expression())
            #print(f"Tipo de retorno encontrado: {return_type}")
            self.return_types.add(return_type)
        else:
            # Si no hay expresión, es un retorno implícito de 'Nil'
            self.return_types.add(NilType())
            #print("Retorno implícito de 'Nil'")
            
        return self.return_types


    # Visit a parse tree produced by CompiscriptParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiscriptParser.WhileStmtContext):
        #print('Visita al nodo de while')
        
        # Crear un nuevo ámbito para el ciclo while
        self.symbol_table.enter_scope()
        
        # Agregar un símbolo únicamente como indicador si un "break" o "continue" es adecuado
        self.symbol_table.add('while', AnyType())
        
        # Código intermedio
        if not self.hasErrors:
            
            # Label para el inicio del bucle
            loop_label = self.code_generator.new_label()
            
            # Agregar la etiqueta de entrada del ciclo a la lista de ciclos
            self.loop_labels.append(loop_label)
            
            # Agregar label de inicio del bucle
            self.code_generator.add_label(loop_label)
        
        # Evaluar la condición del while
        condition_value, condition_type, _ = self.visit(ctx.expression())
        
        # Verificar que la condición sea de tipo booleano
        if not any(isinstance(t, BooleanType) for t in normalize_type(condition_type)):
            #print(f"Adevertencia línea {ctx.start.line}, posición {ctx.start.column}: la condición del bucle 'while' debe ser de tipo booleano")
            self.result.append(f"Adevertencia línea {ctx.start.line}, posición {ctx.start.column}: la condición del bucle 'while' debe ser de tipo booleano")
            
        # Código intermedio
        if not self.hasErrors:
                
                # Label para cuando la condición es falsa
                false_label = self.code_generator.new_label()
                
                # Almacenar la etiqueta de salida en la lista de ciclos
                self.loop_labels_false.append(false_label)
                
                # Agregar salto para el if de MIPS
                # Si la condición es falsa, saltar a la etiqueta false_label
                self.code_generator.add_jump_instruction(false_label, arg1=condition_value, arg2=0)
            
        # Visitar el cuerpo del bucle (solamente si no hay error sintáctico)
        if ctx.statement():
            self.visit(ctx.statement())
            
            # Código intermedio
            if not self.hasErrors:
                    
                    # Agregar salto para regresar al inicio del bucle
                    self.code_generator.add_jump_instruction(loop_label)
                    
                    # Agregar label falso para cuando la condición es falsa
                    self.code_generator.add_label(false_label)
        
                    # Salir del ámbito del ciclo while
                    self.symbol_table.exit_scope()
                    
                    # Quitar la etiqueta de salida del ciclo actual
                    self.loop_labels_false.pop()
        
        # Quitar la etiqueta de entrada del ciclo actual
        self.loop_labels.pop()
        
        return None
    
    def visitBreakStmt(self, ctx: CompiscriptParser.BreakStmtContext):
        # Verificar si se está en un contexto de ciclo
        current_while = self.symbol_table.lookup("while")
        current_for = self.symbol_table.lookup("for")
        
        if not current_while and not current_for:
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'this' se está utilizando fuera de un contexto de clase.")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'break' se está utilizando fuera de un ciclo.")
            self.hasErrors = True
            return None, None, None
        
        # Código intermedio
        
        if not self.hasErrors:
            
            # Obtener la última etiqueta de salida del ciclo
            false_label = self.loop_labels_false[-1]
            
            # Código intermedio: saltar a la etiqueta de salida del ciclo
            self.code_generator.add_jump_instruction(false_label)
            
        return
    
    def visitContinueStmt(self, ctx: CompiscriptParser.ContinueStmtContext):
        # Verificar si se está en un contexto de ciclo
        current_while = self.symbol_table.lookup("while")
        current_for = self.symbol_table.lookup("for")
        
        if not current_while and not current_for:
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'this' se está utilizando fuera de un contexto de clase.")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'break' se está utilizando fuera de un ciclo.")
            self.hasErrors = True
            return None, None, None
        
        # Código intermedio
        
        if not self.hasErrors:
            
            # Obtener la última etiqueta de inicio del ciclo
            loop_label = self.loop_labels[-1]
            
            # Código intermedio: saltar a la etiqueta de inicio del ciclo
            self.code_generator.add_jump_instruction(loop_label)
        
        return

    # Visit a parse tree produced by CompiscriptParser#block.
    def visitBlock(self, ctx:CompiscriptParser.BlockContext):
        self.code_generator.local_pointer = 0
        self.symbol_table.enter_scope()
        result = self.visitChildren(ctx)
        self.symbol_table.exit_scope()
        self.code_generator.global_pointer += self.code_generator.local_pointer
        self.code_generator.local_pointer = 0
        return result


    # Visit a parse tree produced by CompiscriptParser#expression.
    def visitExpression(self, ctx:CompiscriptParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiscriptParser#assignment.
    def visitAssignment(self, ctx:CompiscriptParser.AssignmentContext):
        #print('Visita al nodo de asignación')
        var_name = None
        var_value = None
        var_type = AnyType()
        
        
        call_node = ctx.call()  # Intenta obtener el nodo de llamada a función
    
        if ctx.IDENTIFIER(): # Ya se obtuvo el valor a asignar
            
            var_name = ctx.IDENTIFIER().getText()
            
            if call_node is not None: # Se está llamando a una función o a una propiedad de una clase
                
                # Obtener el valor de retorno de call
                call_value, call_type, call_name = self.visit(call_node)
                
                #print(f"Valor de retorno de la llamada a función: {call_name}")
                
                if call_name == 'this': # Se está haciendo referencia a un método o field de la clase actual
                    current_class = self.symbol_table.lookup('this')
                    current_class.type.add_field(var_name, AnyType())
                    #print(current_class)
                    
                 # Obtener el valor y tipo de la variable de la siguiente asignación
                
                if ctx.assignment(): # Evitar error sintáctico
                    
                    var_value, var_type, _ = self.visit(ctx.assignment())
                    # Determinar el tipo del valor que está siendo asignado
                    #print(f"Se asigna a la propiedad {var_name} de tipo {var_type} el valor {var_value}")
                    
                return var_value, var_type, var_name
            
            # Buscar la variable en la tabla de símbolos
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol is None: # La variable no ha sido declarada
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} no ha sido declarada")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la variable {var_name} no ha sido declarada")
                self.hasErrors = True
                
            else:
                
                # Obtener el valor y tipo de la variable de la siguiente asignación
                
                if ctx.assignment(): # Evitar error sintáctico
                    
                    var_value, var_type, _ = self.visit(ctx.assignment())
                    # Determinar el tipo del valor que está siendo asignado
                    symbol.type = var_type
                    #print(f"Variable {var_name} de tipo {var_type} asignada con valor {var_value}")
                    
                    if not self.hasErrors:
                        self.code_generator.add_instruction(op='=', dest=symbol, arg1=var_value)
                
        elif ctx.logic_or(): # Se sigue con logic_or
            
            var_value, var_type, var_name = self.visit(ctx.logic_or())
            
        return var_value, var_type, var_name


    # Visit a parse tree produced by CompiscriptParser#logic_or.
    def visitLogic_or(self, ctx:CompiscriptParser.Logic_orContext):
        left_value, left_type, left_name = self.visit(ctx.logic_and(0))
        
         # Código intermedio
            
        if not self.hasErrors and len(ctx.logic_and()) > 1:
            
            # Label para cuando alguna de las condiciones es verdadera
            true_label = self.code_generator.new_label()
            
            # Agregar salto para el if de MIPS
            # Si la condición es falsa, saltar a la etiqueta false_label
            self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=1)
        
        for i in range(1, len(ctx.logic_and())):
            right_value, right_type, right_name = self.visit(ctx.logic_and(i))
            
            # Verificar si cualquiera de los conjuntos contiene tipos incompatibles
            if not types_are_boolean(left_type, right_type):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador lógico OR deben ser de tipo 'boolean'")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador lógico OR deben ser de tipo 'boolean'")
                self.hasErrors = True
                return None, NilType(), None
            
            left_type = BooleanType()
            
            # Código intermedio
            
            if not self.hasErrors:
                
                # Si la condición es verdadera, saltar a la etiqueta true_label
                self.code_generator.add_jump_instruction(true_label, arg1=right_value, arg2=1)
                
        # Código intermedio
        if not self.hasErrors and len(ctx.logic_and()) > 1:
            result_temp_name = self.symbol_table.add_temp()
            
            # Si se llega a este punto, todas las condiciones son falsas
            false_label = self.code_generator.new_label()
            self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
            self.code_generator.add_jump_instruction(false_label)
            
            # Agregar label para cuando alguna de las condiciones es verdadera
            self.code_generator.add_label(true_label)
            self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
            
            # Agregar label falso
            self.code_generator.add_label(false_label)
            
            left_value = result_temp_name
            
        return left_value, left_type, left_name

    # Visit a parse tree produced by CompiscriptParser#logic_and.
    def visitLogic_and(self, ctx:CompiscriptParser.Logic_andContext):
        left_value, left_type, left_name = self.visit(ctx.equality(0))
        
        # Código intermedio
            
        if not self.hasErrors and len(ctx.equality()) > 1:
            
            # Label para cuando alguna de las condiciones es falsa
            false_label = self.code_generator.new_label()
            
            # Agregar salto para el if de MIPS
            # Si la condición es falsa, saltar a la etiqueta false_label
            self.code_generator.add_jump_instruction(false_label, arg1=left_value, arg2=0)
        
        for i in range(1, len(ctx.equality())):
            right_value, right_type, right_name = self.visit(ctx.equality(i))
            
            # Verificar si cualquiera de los conjuntos contiene tipos incompatibles
            if not types_are_boolean(left_type, right_type):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador lógico OR deben ser de tipo 'boolean'")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador lógico OR deben ser de tipo 'boolean'")
                self.hasErrors = True
                return None, NilType(), None
            
            left_type = BooleanType()
            
            # Código intermedio
            
            if not self.hasErrors:
                
                # Si la condición es falsa, saltar a la etiqueta false_label
                self.code_generator.add_jump_instruction(false_label, arg1=right_value, arg2=0)
                
                
        # Código intermedio
        if not self.hasErrors and len(ctx.equality()) > 1:
            result_temp_name = self.symbol_table.add_temp()
            
            # Si se llega a este punto, todas las condiciones son verdaderas
            true_label = self.code_generator.new_label()
            self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
            self.code_generator.add_jump_instruction(true_label)
            
            # Agregar label para cuando alguna de las condiciones es falsa
            self.code_generator.add_label(false_label)
            self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
            
            # Agregar label verdadero
            self.code_generator.add_label(true_label)
            
            left_value = result_temp_name
            
        return left_value, left_type, left_name


    # Visit a parse tree produced by CompiscriptParser#equality.
    def visitEquality(self, ctx:CompiscriptParser.EqualityContext):
        #print('Visita al nodo de igualdad')
        
        left_value, left_type, left_name = self.visit(ctx.comparison(0))
        
        for i in range(1, len(ctx.comparison())):
            
            operator = ctx.getChild(2 * i - 1).getText()
            
            right_value, right_type, right_name = self.visit(ctx.comparison(i))
            
            # Validar si los tipos son compatibles
            if not types_are_compatible(left_type, right_type):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador de igualdad deben ser del mismo tipo o compatibles")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador de igualdad deben ser del mismo tipo o compatibles")
                self.hasErrors = True
                return None, NilType(), None
                
            left_type = BooleanType()  # El resultado de una igualdad es siempre booleano
            
            # Código intermedio
            
            if not self.hasErrors:
                
                if operator == '==':
                    
                    true_label = self.code_generator.new_label() # Label para cuando la expresión es verdadera
                    false_label = self.code_generator.new_label() # Label para cuando la expresión es falsa
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la igualdad
                    
                    # Si es igual, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value)
                    
                    # Si no es igual, el resultado es falso
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    self.code_generator.add_jump_instruction(false_label)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    
                    # Agregar label falso
                    self.code_generator.add_label(false_label)
                    
                    
                elif operator == '!=':
                    false_label = self.code_generator.new_label() # Label para cuando la expresión es falsa
                    true_label = self.code_generator.new_label() # Label para cuando la expresión es verdadera
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la igualdad
                    
                    # Si es igual, el resultado es falso
                    self.code_generator.add_jump_instruction(false_label, arg1=left_value, arg2=right_value)
                    
                    # Si no es igual, el resultado es verdadero
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    self.code_generator.add_jump_instruction(true_label)
                    
                    # Agregar label falso
                    self.code_generator.add_label(false_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                
                left_value = result_temp_name
            
        return left_value, left_type, left_name


    # Visit a parse tree produced by CompiscriptParser#comparison.
    def visitComparison(self, ctx:CompiscriptParser.ComparisonContext):
        #print('Visita al nodo de comparación')
        
        left_value, left_type, left_name = self.visit(ctx.term(0))
        
        for i in range(1, len(ctx.term())):
            operator = ctx.getChild(2 * i - 1).getText()
            
            right_value, right_type, right_name = self.visit(ctx.term(i))
            
            # Validar si los tipos son numéricos
            if not types_are_numeric(left_type, right_type):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador de comparación deben ser numéricos")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador de comparación deben ser numéricos")
                self.hasErrors = True
                return None, NilType(), None
                    
            left_type = BooleanType()  # El resultado de una comparación es siempre booleano
            
            # Código intermedio
            
            if not self.hasErrors:
                
                # Añadir saltos para el if de MIPS
                
                false_label = self.code_generator.new_label() # Label para cuando la expresión es falsa
                true_label = self.code_generator.new_label() # Label para cuando la expresión es verdadera
                
                
                if operator == '<':
                    
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la comparación
                    
                    # Si es menor que, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value, op='<')
                    
                    # Si no es menor que, el resultado es falso
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    self.code_generator.add_jump_instruction(false_label)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(false_label)
                    
                elif operator == '<=':
                    
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la comparación
                    
                    # Si es menor que, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value, op='<')
                    
                    # Si es igual, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value)
                    
                    # Si no es menor que, el resultado es falso
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    self.code_generator.add_jump_instruction(false_label)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(false_label)
                    
                elif operator == '>':
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la comparación
                    
                    # Si es mayor que, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value, op='>')
                    
                    # Si no es mayor que, el resultado es falso
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    self.code_generator.add_jump_instruction(false_label)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(false_label)
                    
                elif operator == '>=':
                    result_temp_name = self.symbol_table.add_temp() # Temporal para guardar el resultado de la comparación
                    
                    # Si es mayor que, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value, op='>')
                    
                    # Si es igual, el resultado es verdadero
                    self.code_generator.add_jump_instruction(true_label, arg1=left_value, arg2=right_value)
                    
                    # Si no es menor que, el resultado es falso
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=0)
                    self.code_generator.add_jump_instruction(false_label)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(true_label)
                    self.code_generator.add_instruction(op='=', dest=result_temp_name, arg1=1)
                    
                    # Agregar label verdadero
                    self.code_generator.add_label(false_label)
                
                left_value = result_temp_name
            
        return left_value, left_type, left_name


    # Visit a parse tree produced by CompiscriptParser#term.
    def visitTerm(self, ctx:CompiscriptParser.TermContext):
        #print('Visita al nodo de término')
        
        left_value, left_type, left_name = self.visit(ctx.factor(0))
        
        for i in range(1, len(ctx.factor())):
            
            right_value, right_type, right_name = self.visit(ctx.factor(i))
            print('right value: ', right_value)
            
            operator = ctx.getChild(2 * i - 1).getText()
            
            if operator == '+':
                
                op = 'ADD'
                
                numeric_types = types_are_numeric(left_type, right_type)
                string_types = types_are_string(left_type, right_type) # Tomar en consideración concatencación?
                    
                if not numeric_types:
                    #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de una suma deben ser ambos numéricos o ambos cadenas")
                    self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: los operandos de una suma deben ser numéricos")
                    self.hasErrors = True
                    return None, NilType(), None
                
                left_type = NumberType()
                
            elif operator == '-':
                
                op = 'SUB'
                
                if not types_are_numeric(left_type, right_type):
                    #print(f"Advertencia línea {ctx.start.line}, posición {ctx.start.column}: los operandos de una resta deben ser numéricos")
                    self.result.append(f"Advertencia línea {ctx.start.line}, posición {ctx.start.column}: los operandos de una resta deben ser numéricos")
                    return None, NilType(), None
                
                left_type = NumberType()
                
            # Código intermedio
                
            if not self.hasErrors:
                result_temp_name = self.symbol_table.add_temp()
                self.code_generator.add_instruction(op=op, dest=result_temp_name, arg1=left_value, arg2=right_value)
                
                left_value = result_temp_name
            
        return left_value, left_type, left_name


    # Visit a parse tree produced by CompiscriptParser#factor.
    def visitFactor(self, ctx:CompiscriptParser.FactorContext):
        #print('Visita al nodo de factor')
        
        left_value, left_type, left_name = self.visit(ctx.unary(0))
        
        #print('Valor de retorno de unary: ', left_value)
        
        for i in range(1, len(ctx.unary())):

            right_value, right_type, right_name = self.visit(ctx.unary(i))
            
            operator = ctx.getChild(2 * i - 1).getText()
            
            # Validar si los tipos son numéricos
            if not types_are_numeric(left_type, right_type):
                #print(f"Error semántico {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador aritmético deben ser numéricos")
                self.result.append(f"Error semántico {ctx.start.line}, posición {ctx.start.column}: los operandos de un operador aritmético deben ser numéricos")
                self.hasErrors = True
                return None, NilType(), None
            
            if not self.hasErrors:
                if operator == '*':
                    op = 'MUL'
                elif operator == '/':
                    op = 'DIV'
                elif operator == '%':
                    op = 'MOD'
                
                # Temporal para el resultado
                result_temp_name = self.symbol_table.add_temp()
                self.code_generator.add_instruction(op=op, dest=result_temp_name, arg1=left_value, arg2=right_value)
                
                left_value = result_temp_name
                    
            else:
                left_value = None
                
            left_type = NumberType()
            
            
        return left_value, left_type, left_name
    
    # Visit a parse tree produced by CompiscriptParser#array.
    def visitArray(self, ctx:CompiscriptParser.ArrayContext):
        #print('Visita al nodo de arreglo')
        types = set()
        
        for expression in ctx.expression():
            value, type, _ = self.visit(expression)
            types.add(type)
        
        #print('Tipos del arreglo: ', types)
        
        return types


    # Visit a parse tree produced by CompiscriptParser#instantiation.
    def visitInstantiation(self, ctx:CompiscriptParser.InstantiationContext):
        # Obtener el nombre de la clase
        #print('Visita al nodo de instanciación')
        class_name = ctx.IDENTIFIER().getText()
        
        # Verificar si la clase ha sido declarada
        class_symbol = self.symbol_table.lookup(class_name)
        
        if not class_symbol:
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {class_name} no ha sido declarada")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {class_name} no ha sido declarada")
            self.hasErrors = True
            return None, None, None
        
        arguments = []
        if ctx.arguments():
            arguments = self.visit(ctx.arguments())
            
        if class_symbol.type.methods['init']:
            if len(arguments) != len(class_symbol.type.methods['init'].arg_types):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {class_name} espera {len(class_symbol.type.methods['init'].arg_types)} argumentos, pero se pasaron {len(arguments)}")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {class_name} espera {len(class_symbol.type.methods['init'].arg_types)} argumentos, pero se pasaron {len(arguments)}")
                self.hasErrors = True
                
        # Crear una instancia de la clase
        instance = InstanceType(class_symbol.type, arguments)
        
        return None, instance, None


    # Visit a parse tree produced by CompiscriptParser#unary.
    def visitUnary(self, ctx:CompiscriptParser.UnaryContext):
        #print('Visita al nodo de operador unario')
        
        # Caso 1: es un operador unario
        if ctx.getChildCount() == 2:  # Esto indica que hay un operador unario seguido por otro unary
            operator = ctx.getChild(0).getText()
            value, value_type, _ = self.visit(ctx.unary())
            
            # Verificar que el tipo del valor sea compatible con el operador
            if operator == '!':
                if not (any(isinstance(t, BooleanType) or any(isinstance(t, AnyType))) for t in normalize_type(value_type)):
                    #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el operador '!' solo se puede aplicar a booleanos")
                    self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el operador '!' solo se puede aplicar a booleanos")
                    self.hasErrors = True
                    return None, NilType(), None
                
                result_type = BooleanType()
                
                # Código intermedio
                
                if not self.hasErrors:
                    
                    temp_name = self.code_generator.symbol_table.add_temp()
                    self.code_generator.add_instruction(op='NOR', dest=temp_name, arg1=value)
                    result_value = temp_name
            
            elif operator == '-':
                if not (any(isinstance(t, NumberType) or any(isinstance(t, AnyType))) for t in normalize_type(value_type)):
                    #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el operador '-' solo se puede aplicar a números")
                    self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el operador '-' solo se puede aplicar a números")
                    self.hasErrors = True
                    return None, NilType(), None
                result_type = NumberType()
                
                # Código intermedio
                
                if not self.hasErrors:
                    
                    temp_name = self.symbol_table.add_temp()
                    self.code_generator.add_instruction(op='NEG', dest=temp_name, arg1=value)
                    result_value = temp_name
            
            return result_value, result_type, None
        
        # Caso 2: es una llamada a función u otra expresión primaria
        else:
            return self.visit(ctx.call())


    # Visit a parse tree produced by CompiscriptParser#call.
    def visitCall(self, ctx:CompiscriptParser.CallContext):
        #print("Visita al nodo de llamada a función")

        # Obtener el nombre de primary
        value, type, name = self.visit(ctx.primary())
        
        #print(ctx.getText())
        
        if value == 'this': # Se está llamando a un método o field de la clase actual
            
            # Verificar si existe dicha clase actual (this)
            current_class = self.symbol_table.lookup("this")
            
            if not current_class:
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'this' se está utilizando fuera de un contexto de clase.")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'this' se está utilizando fuera de un contexto de clase.")
                self.hasErrors = True
                return None, None, None
            
        if '.' in ctx.getText() and not (isinstance(type, NumberType) or isinstance(type, StringType)) and not ctx.getText().startswith('super'): # Se está llamando a un método o field de una clase
            # Dado que los fields y métodos de una clase pueden cambiar en tiempo de ejecución,
            # únicamente se asume que el valor de retorno es de tipo 'Any' y advertir si se trata de una instancia
            
            if not isinstance(type, InstanceType) and name != "this":
                #print(f'Error semántico línea {ctx.start.line}, posición {ctx.start.column}: "{name}" no se trata de una instancia')
                self.result.append(f'Error semántico línea {ctx.start.line}, posición {ctx.start.column}: "{name}" no se trata de una instancia')
                self.hasErrors = True
                
                return None, AnyType(), name
            
            """ if isinstance(type, InstanceType):
                previousIdentifierTypeInstance = True
                for i in range(0, len(ctx.IDENTIFIER())): # Recorrer los métodos y fields de la clase
                    
                    if not previousIdentifierTypeInstance:
                        #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador {ctx.IDENTIFIER(i - 1)} no es una instancia")
                        self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el identificador {ctx.IDENTIFIER(i - 1)} no es una instancia")
                        return None, None, None
                
                    #print('CALL IDENTIFIER: ', ctx.IDENTIFIER(i).getText())
                    
                    field_name = ctx.IDENTIFIER(i).getText()
                    
                    #print('FIELD NAME: ', field_name)
                    #print(type.class_type.superclass.get_method(field_name))
                    if not type.class_type.get_field(field_name) and not type.class_type.get_method(field_name) and not type.class_type.superclass.get_field(field_name) and not type.class_type.superclass.get_method(field_name):
                        #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {type.name} no tiene un field '{field_name}'")
                        self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase {type.name} no tiene un field '{field_name}'")
                        return None, None, None
                    
                    previousIdentifierTypeInstance = type.class_type.get_field(field_name) or type.class_type.get_method(field_name) or type.class_type.superclass.get_field(field_name) or type.class_type.superclass.get_method(field_name)
                    previousIdentifierTypeInstance = isinstance(previousIdentifierTypeInstance, InstanceType)
                    
                    #print('PREVIOUS IDENTIFIER TYPE: ', previousIdentifierTypeInstance)
            
            return None, AnyType(), name """
        
        if type is None: # No acarrear errores semánticos
            return None, None, None
        
        # Si no se trata de una función, devolver primary
        if not (isinstance(type, FunctionType) or isinstance(type, AnonymousFunctionType)):
            return value, type, name
        
        # Buscar la función en la tabla de símbolos
        function_symbol = self.symbol_table.lookup(name)

        if not function_symbol:
            #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: La función '{name}' no ha sido declarada.")
            self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: La función '{name}' no ha sido declarada.")
            self.hasErrors = True
            return None, None, None
        
        if '(' not in ctx.getText(): # Se está haciendo referencia a una función, no a una llamada
            return_type = function_symbol.type
            
        else:
            return_type = function_symbol.type.return_type

        # Validar los argumentos pasados a la función
        arguments = []
        if ctx.arguments():
            for arg in ctx.arguments():
                arguments = self.visit(arg)

        if len(arguments) != len(function_symbol.type.arg_types):
            #print(f"Error semántico: La función '{name}' espera {len(function_symbol.type.arg_types)} argumentos, pero se pasaron {len(arguments)}.")
            self.result.append(f"Error semántico: La función '{name}' espera {len(function_symbol.type.arg_types)} argumentos, pero se pasaron {len(arguments)}.")
            self.hasErrors = True
            return None, None, None

        return None, return_type, name


    # Visit a parse tree produced by CompiscriptParser#primary.
    def visitPrimary(self, ctx:CompiscriptParser.PrimaryContext):
        #print('Visita al nodo de primary')
        # result = self.visitChildren(ctx)
        value = None
        type = AnyType()
        var_name = None
        
        if ctx.NUMBER():
            value = float(ctx.NUMBER().getText())
            type = NumberType()
                
        elif ctx.STRING():
            value = ctx.STRING().getText()
            type = StringType()
                
        elif ctx.expression(): # Si es una expresión
            value, type, var_name = self.visit(ctx.expression())
                
        elif ctx.getText() == 'nil':
            value = None
            type = NilType()
        
        elif ctx.getText() == 'true':
            value = True
            type = BooleanType()
            
        elif ctx.getText() == 'false':
            value = False
            type = BooleanType()
            
        elif ctx.getText() == 'this':
            value = 'this'
            type = ClassType('this')
            var_name = 'this'
            
        elif ctx.funAnon():
            #print('Primary reconoce función anónima')
            type = self.visit(ctx.funAnon())  # Visita la función anónima
            
        elif ctx.array(): # Si es un arreglo
            #print('Primary reconoce arreglo')
            type = self.visit(ctx.array()) # Visita el arreglo
            
        elif ctx.instantiation(): # Si es una instancia
            #print('Primary reconoce instancia')
            value, type, var_name = self.visit(ctx.instantiation())
            
        elif ctx.getText().startswith('super'):
            #print('Visita al nodo de super')
            # Encontrar la clase actual
            current_class = self.symbol_table.lookup('this')
            
            #print('SUPER: Clase actual: ', current_class)
            
            if not current_class:
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'super' se está utilizando fuera de un contexto de clase.")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'super' se está utilizando fuera de un contexto de clase.")
                self.hasErrors = True
                return None, None, None
            
            if not isinstance(current_class.type, ClassType):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'super' se está utilizando fuera de un contexto de clase.")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: 'super' se está utilizando fuera de un contexto de clase.")
                self.hasErrors = True
                return None, None, None
            
            if not current_class.type.superclass:
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase actual no tiene superclase.")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: la clase actual no tiene superclase.")
                self.hasErrors = True
                return None, None, None
            

            # Obtener el método de la superclase
            method_name = ctx.IDENTIFIER().getText()
            superclass = current_class.type.superclass
            method = superclass.get_method(method_name)
            #print('Tipo del Método encontrado: ', method)

            if not method:
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el método {method_name} no existe en la superclase {superclass.name}.")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el método {method_name} no existe en la superclase {superclass.name}.")
                self.hasErrors = True
                return None, None, None

            #print(f"Llamada al método {method_name} en superclase {superclass.name}.")
            return None, method.return_type, f'super.{method_name}'
                
        elif ctx.IDENTIFIER(): # Si es un identificador
            #print('Lo reconoce como identificador')
            var_name = ctx.IDENTIFIER().getText()
            symbol = self.symbol_table.lookup(var_name)
            
            if symbol:
                value = symbol
                type = symbol.type
                #print(f"{var_name} encontrada con tipo {type} y valor {value}")
                
            else:
                #print(f'Error semántico línea {ctx.start.line}, posición {ctx.start.column}: "{var_name}" no ha sido declarada')
                self.result.append(f'Error semántico línea {ctx.start.line}, posición {ctx.start.column}: "{var_name}" no ha sido declarada')
                self.hasErrors = True
        
        return value, type, var_name
            

    # Visit a parse tree produced by CompiscriptParser#function.
    def visitFunction(self, ctx:CompiscriptParser.FunctionContext):
        #print('Visita al nodo de función')
        
        function_name = ctx.IDENTIFIER().getText()
            
        # El tipo de retorno de la función es 'Nil' por defecto.
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
            #print(f"Tipos de retorno de la función {function_name}: {function_type.return_type}")
            
        # Limpiar la lista de tipos de retorno para esta función
        self.return_types = set()
        
        return function_name, function_type
    
    
    # Visit a parse tree produced by CompiscriptParser#funAnon.
    def visitFunAnon(self, ctx:CompiscriptParser.FunAnonContext):
        #print('Visita al nodo de función anónima')
        
        # El tipo de retorno de la función es 'nil' por defecto.
        return_type = AnyType()
        
        # Crear un nuevo ámbito para los parámetros de la función anónima
        self.symbol_table.enter_scope()
        
        # Obtener los parámetros de la función anónima
        parameters = []
        if ctx.parameters():
            parameters = self.visit(ctx.parameters())
        
        # Crear un tipo para la función anónima
        function_type = AnonymousFunctionType(return_type, parameters)
        
        # Visitar el bloque de la función anónima
        self.visit(ctx.block())
        
        # Salir del ámbito de los parámetros
        self.symbol_table.exit_scope()
        
        # Determinar si la función anónima tiene uno o más valores de retorno
        if self.return_types:
            function_type.return_type = self.return_types
            #print(f"Tipos de retorno de la función anónima: {function_type.return_type}")
        
        # Limpiar la lista de tipos de retorno para esta función
        self.return_types = set()
        
        return function_type  # Devolver el tipo de la función anónima


    # Visit a parse tree produced by CompiscriptParser#parameters.
    def visitParameters(self, ctx:CompiscriptParser.ParametersContext):
        parameters = []
    
        # Iterar sobre cada IDENTIFIER en el contexto
        for i in range(len(ctx.IDENTIFIER())):
            param_name = ctx.IDENTIFIER(i).getText()
            #print(f"Parámetro encontrado: {param_name}")
            
            if self.symbol_table.lookup(param_name):
                #print(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el parámetro {param_name} ya ha sido declarado en este ámbito")
                self.result.append(f"Error semántico línea {ctx.start.line}, posición {ctx.start.column}: el parámetro {param_name} ya ha sido declarado en este ámbito")
                self.hasErrors = True
            else:
                parameters.append(AnyType())
                #print(f"Parámetro encontrado: {param_name}")
                self.symbol_table.add(param_name, AnyType())
            
        return parameters


    # Visit a parse tree produced by CompiscriptParser#arguments.
    def visitArguments(self, ctx:CompiscriptParser.ArgumentsContext):
        #print("Visita al nodo de argumentos")
        arguments = []
        
        # Iterar sobre cada expression en el contexto
        for i in range(len(ctx.expression())):
            argument = self.visit(ctx.expression(i))
            #print('Argumento: ', argument)
            arguments.append(argument)
            #print(f"Argumento encontrado: {argument}")
            
        #print('Terminando la visita al nodo de argumentos')
            
        return arguments