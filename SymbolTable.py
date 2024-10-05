import uuid
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        
    def add(self, name, symbol):
        self.symbols[name] = symbol
        
    def lookup(self, name):
        if name in self.symbols:
            return self.symbols[name]
        elif self.parent:
            return self.parent.lookup(name)
        else:
            return None
        
class Symbol:
    def __init__(self, name, type, global_offset=None, local_offset=None, value=None):
        self.name = name
        self.type = type
        self.global_offset = global_offset
        self.local_offset = local_offset
        self.value = value
        
    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.type}, GP[{self.global_offset}], LP[{self.local_offset}])"
    
class TempSymbol(Symbol):
    def __init__(self, name, global_offset=None, local_offset=None, value=None):
        # Llamar al constructor de la clase base (Symbol)
        super().__init__(name, type="temp", global_offset=global_offset, local_offset=local_offset, value=value)
        
    def __repr__(self):
        return f'{self.name.split("-")[:1][0]}'
    
class AnyType:
    def __init__(self):
        self.name = "any"
        
    def __repr__(self):
        return "AnyType()"        
class NumberType:
    def __init__(self):
        self.name = "number"
        
    def __repr__(self):
        return "NumberType()"
    
class BooleanType:
    def __init__(self):
        self.name = "boolean"
        
    def __repr__(self):
        return "BooleanType()"
    
class StringType:
    def __init__(self):
        self.name = "string"
        
    def __repr__(self):
        return "StringType()"
    
class NilType:
    def __init__(self):
        self.name = "nil"
        
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
        self.methods = {}
        self.fields = {}
        
    def add_method(self, name, method_type):
        self.methods[name] = method_type

    def add_field(self, name, field_type):
        self.fields[name] = field_type

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
        
    def get_field(self, name):
        return self.fields.get(name)
        
    def __repr__(self):
        return f"InstanceType(class_type={self.class_type}, fields={self.fields})"

class ListSymbolTable:
    def __init__(self):
        self.scopes = [SymbolTable()]
        self.current_global_offset = 0
        self.current_local_offset = 0
        self.temp_count = 0
        
    def enter_scope(self):
        parent_scope = self.current_scope()
        new_scope = SymbolTable(parent=parent_scope)
        self.scopes.append(new_scope)
        
    def exit_scope(self):
        self.scopes.pop()
    
    def current_scope(self):
        return self.scopes[-1]
    
    def add(self, name, type, global_offset=None, local_offset=None, value=None):
        symbol = Symbol(name, type, global_offset, local_offset, value)
        self.current_scope().add(name, symbol)
        return symbol
        
    def delete(self, name):
        self.current_scope().symbols.pop(name)
        
    def lookup(self, name):
        return self.current_scope().lookup(name)
    
    def add_temp(self, global_offset=None, local_offset=None, value=None):
        name = f"t{self.temp_count}-{uuid.uuid4()}"
        symbol = TempSymbol(name, global_offset, local_offset, value)
        self.current_scope().add(name, symbol)
        self.temp_count += 1
        return symbol
