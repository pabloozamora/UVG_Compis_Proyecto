import uuid

POINTER_SIZE = 4
CLASS_SIZE = 255
class SymbolTable:
    def __init__(self, parent=None, function_scope=False):
        self.symbols = {}
        self.parent = parent
        self.function_scope = function_scope
        self.scope_offset = parent.scope_offset if parent and not self.function_scope else 0
        
    def add(self, name, symbol):
        self.symbols[name] = symbol
        
        if not (isinstance(symbol.type, FunctionType) or isinstance(symbol.type, AnonymousFunctionType)):
            self.scope_offset += POINTER_SIZE
        
    def lookup(self, name, params=None):
        if name in self.symbols:
            if params:
                symbol = self.symbols[name]
                if isinstance(symbol.type, FunctionType) or isinstance(symbol.type, AnonymousFunctionType):
                    if len(params) == len(symbol.type.arg_types):
                        return symbol
                    else:
                        return None
                else:
                    return None
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return None
        
    def in_function_scope(self):
        if self.function_scope:
            return True
        elif self.parent:
            return self.parent.in_function_scope()
        else:
            return False
        
class Symbol:
    def __init__(self, name, type, offset=None, scope="GP", value=None):
        self.name = name
        self.type = type
        self.offset = offset
        self.scope = scope
        self.value = value
        self.id = f'{uuid.uuid4()}'
        
    def __repr__(self):
        if isinstance(self.type, dict) or isinstance(self.type, set):
            return f"Symbol(name={self.name}, type={[typeObj for typeObj in self.type]}, {self.scope}[{self.offset}])"
        return f"Symbol(name={self.name}, type={self.type.name}, {self.scope}[{self.offset}])"
    
class TempSymbol(Symbol):
    def __init__(self, name, type="temp", offset=None, scope="GP", value=None):
        # Llamar al constructor de la clase base (Symbol)
        super().__init__(name, type=type, offset=offset, scope=scope, value=value)
        
    def __repr__(self):
        return f'{self.name.split("-")[:1][0]} ({self.scope}[{self.offset}])'
    
class AnyType:
    def __init__(self):
        self.name = "any"
        
    def __repr__(self):
        return "AnyType()"        
class NumberType:
    def __init__(self, is_float=True):
        self.name = "number"
        self.size = 4
        self.is_float = is_float
        
    def __repr__(self):
        return "NumberType()"
    
class BooleanType:
    def __init__(self):
        self.name = "boolean"
        self.size = 4
        
    def __repr__(self):
        return "BooleanType()"
    
class StringType:
    def __init__(self):
        self.name = "string"
        self.size = 255
        
    def __repr__(self):
        return "StringType()"
    
class NilType:
    def __init__(self):
        self.name = "nil"
        self.size = 1
        
    def __repr__(self):
        return "NilType()"
    
class FunctionType:
    def __init__(self, return_type, arg_types):
        self.name = "function"
        self.return_type = return_type
        self.arg_types = arg_types
        
    def __repr__(self):
        return f"FunctionType(return_type={self.return_type}, arg_types={self.arg_types})"
    
class AnonymousFunctionType:
    def __init__(self, return_type, arg_types):
        self.name = "function"
        self.return_type = return_type
        self.arg_types = arg_types
        
    def __repr__(self):
        return f"AnonymousFunctionType(return_type={self.return_type}, arg_types={self.arg_types})"
    
class ClassType:
    def __init__(self, name, superclass=None):
        self.name = name
        self.superclass = superclass
        self.current_offset = 0
        self.methods = {}
        self.fields = {}
        self.size = CLASS_SIZE
        
    def add_method(self, name, method_type):
        self.methods[name] = method_type

    def add_field(self, name, field_type):
        if name in self.fields:
            existing_field = self.fields.get(name)
            self.fields[name] = {'type': field_type, 'offset': existing_field['offset']}
            return
        self.fields[name] = {'type': field_type, 'offset': self.current_offset}
        self.current_offset += POINTER_SIZE

    def get_method(self, name):
        return self.methods.get(name)

    def get_field(self, name):
        return self.fields.get(name)
        
    def __repr__(self):
        return f"ClassType(name={self.name}, fields={self.fields}, methods={self.methods} superclass={self.superclass})"
    
class InstanceType:
    def __init__(self, class_type=None, init_arguments=None):
        self.name = class_type.name
        self.class_type = class_type
        self.fields = {}
        self.init_arguments = init_arguments or []
        self.current_offset = 0
        self.size = 4
        
    def add_field(self, name, field_type):
        self.fields[name] = {'type': field_type, 'offset': self.current_offset}
        self.current_offset += POINTER_SIZE
        
    def get_field(self, name):
        return self.fields.get(name)
        
    def __repr__(self):
        return f"InstanceType(class_type={self.class_type}, fields={self.fields})"

class ListSymbolTable:
    def __init__(self):
        self.scopes = [SymbolTable()]
        self.temp_count = 0
        
    def enter_scope(self, function_scope=False):
        parent_scope = self.current_scope()
        new_scope = SymbolTable(parent=parent_scope, function_scope=function_scope)
        self.scopes.append(new_scope)
        
    def exit_scope(self): # Tomar en cuenta si el scope actual es de función y si el scope hijo es de función
        exiting_scope = self.scopes.pop()
        if not exiting_scope.in_function_scope():
            self.current_scope().scope_offset = exiting_scope.scope_offset
    
    def current_scope(self):
        return self.scopes[-1]
    
    def in_function_scope(self):
        return self.current_scope().in_function_scope()
    
    def add(self, name, type, value=None):
        symbol_offset = self.current_scope().scope_offset
        symbol_scope = 'GP'
        if self.in_function_scope():
            symbol_scope = 'SP'
        symbol = Symbol(name, type, offset=symbol_offset, scope=symbol_scope, value=value)
        self.current_scope().add(name, symbol)
        return symbol
        
    def delete(self, name):
        self.current_scope().symbols.pop(name)
        
    def lookup(self, name):
        return self.current_scope().lookup(name)
    
    def add_temp(self, type="temp", value=None):
        name = f"t{self.temp_count}-{uuid.uuid4()}"
        symbol_offset = self.current_scope().scope_offset
        symbol_scope = 'GP'
        if self.in_function_scope():
            symbol_scope = 'SP'
        symbol = TempSymbol(name, type=type, offset=symbol_offset, scope=symbol_scope, value=value)
        self.current_scope().add(name, symbol)
        self.temp_count += 1
        return symbol
