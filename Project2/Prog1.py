def predictive_parser( input ):
	parsing_table = {
		'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
        'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
        'T': {'a': ['F', 'R'], '(': ['F', 'R']},
        'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
        'F': {'a': ['a'], '(': ['(', 'E', ')']}
	}

	# Parsing Logic

terminals = ['a', '+', '-', '$', '/', '(', ')', '*']
non_terminals = ['E', 'Q', 'T', 'R', 'F']

# Testing
test_strings = [
	"(a+a)*a$",
	"a*(a/a)$",
	"a(a+a)$"
]
print("\n--- Testing ---")
for string in test_strings:
	print( f"Parsing: { string }")
	predictive_parser( string )
