def predictive_parser(input):
    parsing_table = {
        'E': {'a': ['T', 'Q'], '(': ['T', 'Q']},
        'Q': {'+': ['+', 'T', 'Q'], '-': ['-', 'T', 'Q'], ')': ['ε'], '$': ['ε']},
        'T': {'a': ['F', 'R'], '(': ['F', 'R']},
        'R': {'+': ['ε'], '-': ['ε'], '*': ['*', 'F', 'R'], '/': ['/', 'F', 'R'], ')': ['ε'], '$': ['ε']},
        'F': {'a': ['a'], '(': ['(', 'E', ')']}
    }

    stack = ['$', 'E']
    input += '$'
    index = 0
    derivation = []  # To track the production rules used

    print(f"{'Stack':<20} {'Input':<20} {'Action'}")
    print('-' * 50)

    while len(stack) > 0:
        top = stack[-1]
        current_input = input[index]

        print(f"{''.join(stack):<20} {input[index:]:<20}", end='')

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

