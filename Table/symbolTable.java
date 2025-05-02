// x = 5
// name : x
// type : int
// value : 5
// lod = 1
// scope = global
// role = variable
// size = 4

import java.util.*;

class Symbol {
	String name;
	String type;
	Object value;
	int line;
	String scope;
	String role;
	int size;

	public Symbol(String name, String type, Object value, int line, String scope, String role, int size) {
		this.name = name;
		this.type = type;
		this.value = value;
		this.line = line;
		this.scope = scope;
		this.role = role;
		this.size = size;
	}

	@Override
	public String toString() {
		return "Symbol(" + name + ", " + type + ", " + value + ", " + line + ", " + scope + ", " + role + ", " + size
				+ ", ";
	}
}

class symbolTable {
	private Stack<Map<String, Symbol>> scopeStack;

	public void SymbolTable() {
		scopeStack = new Stack<>();
		scopeStack.push(new HashMap<>());
	}

	private Map<String, Symbol> currentScope() {
		return scopeStack.peek();
	}

	public void insert(String name, String type, Object value, int line, String scope, String role, int size) {
		Map<String, Symbol> current = currentScope();
		if (current.containsKey(name)) {
			throw new RuntimeException("Symbol " + name + "already exists in the current scope.");
		}

		Symbol symbol = new Symbol(name, type, value, line, scope, role, size);
		current.put(name, symbol);
	}
}