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
    def __init__(self, name, type, value=None):
        self.name = name
        self.type = type
        self.value = value
        
    def __repr__(self):
        return f"Symbol(name={self.name}, type={self.type}, value={self.value})"
        
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
        self.return_type = return_type
        self.arg_types = arg_types
        
    def __repr__(self):
        return f"FunctionType(return_type={self.return_type}, arg_types={self.arg_types})"
    
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
        return f"ClassType(name={self.name}, fields={self.fields}, methods={self.methods})"
    
class InstanceType:
    def __init__(self, class_type=None, init_arguments=None):
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
        
    def enter_scope(self):
        parent_scope = self.current_scope()
        new_scope = SymbolTable(parent=parent_scope)
        self.scopes.append(new_scope)
        
    def exit_scope(self):
        self.scopes.pop()
    
    def current_scope(self):
        return self.scopes[-1]
    
    def add(self, name, type, value=None):
        symbol = Symbol(name, type, value)
        self.current_scope().add(name, symbol)
        
    def lookup(self, name):
        return self.current_scope().lookup(name)
