# x = 5
# name : x
# type : int
# value : 5
# lod = 1
# scope = global
# role = variable
# size = 4

class Symbol:
    def __init__(self, name, type, value, line, scope, role, size):
        self.name = name
        self.type = type
        self.value = value
        self.line = line
        self.scope = scope
        self.role = role
        self.size = size

    def __repr__(self):
        return f"Symbol({self.name}, {self.type}, {self.value}, {self.line}, {self.scope}, {self.role}, {self.size})"
    
class SymbolTable:
    def __init__(self):
        self.scope_stack = [{}]

    def current_scope(self):
        return self.scope_stack[-1]
    
    def insert(self, name, type, value, line, scope, role, size):
        current = self.current_scope()
        if name in current:
            raise Exception(f"Symbol {name} already exists in the current scope")
        symbol = Symbol(name=name, type=type, value=value, line=line, scope=scope, role=role, size=size)
        current[name] = symbol # Adding X to the 2nd level/scope

    def lookup(self, name):
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        raise Exception(f"Symbol {name} not found in any scope")
    
    def update(self, name, value, new_value):
        symbol = self.lookup(name)
        if symbol:
            symbol.value = new_value
        else:
            raise Exception(f"Symbol {name} not found in any scope")
        
    def enter_scope(self):
        self.scope_stack.append({})
        print('Entering new scope')

    def exit_scope(self):
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()
            print('Exiting scope')
        else:
            raise Exception("Cannot exit global scope")
        
    def print_table(self):
        for i, scope in enumerate(self.scope_stack):
            print(f"Scope {i}:")
            for name, symbol in scope.items():
                print(f" {name}")
                print()
                
                #remake in java for discussion