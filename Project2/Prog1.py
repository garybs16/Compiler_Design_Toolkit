# PROJECT 2 Report File
# CPSC 323-11: Group 4
# Group Members 
# - Anar Otgonbaatar 
# - Andres Ugalde 
# - Daniel Felix 
# - Gary Samue

def predictive_parser(input):
    parsing_table = {
        'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
        'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
        'T': {'a': ['F', 'R'], '(': ['F', 'R']},
        'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
        'F': {'a': ['a'], '(': ['(', 'E', ')']}
    }

    stack = ['$', 'E']	# Init stack with start symbols
    input += '$'		# Append $ to mark end of input
    index = 0			# Input pointer
    derivation = []  # To track the production rules used

    print(f"{'Stack':<45} {'Input':<15} {'Action'}")
    print('-' * 50)

    while len(stack) > 0:
        top = stack[-1]
        current_input = input[index]

        print(f"{str(stack):<45} {input[index:]:<15}", end='')

        if top == current_input == '$':
            print("Accept")
            print("String Accepted ✅")
            return
        elif top == current_input:
            stack.pop()
            index += 1
            print(f"Match {current_input}")
        elif top in parsing_table:
            production = parsing_table[top].get(current_input)
            if production is None:
                print(f"Error: no rule for ({top}, {current_input})")
                print("Syntax Error ❌")
                return
            else:
                stack.pop()
                if production != ['ε']:
                    stack.extend(reversed(production))
                derivation.append(f"{top} -> {''.join(production)}")
                print(f"Output {top} -> {''.join(production)}")
        else:
            print(f"Error: unexpected symbol {current_input}")
            print("Syntax Error ❌")
            return

    print("String Rejected ❌")

test_strings = ["(a+a)*a", "a*(a/a)", "a(a+a)"]
for string in test_strings:
    print( f"\nInput: { string }" )
    predictive_parser( string )