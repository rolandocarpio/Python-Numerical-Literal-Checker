# Task 3: Recognizing Floating Point Literals

def is_float(input_str):
    # Define transition table for floating point literals
    transitions = {
        0: {'digit': 1, '.': 2},                   # From state 0, if input is a digit or '.', transition to state 1 or 2
        1: {'digit': 1, '.': 3, 'eE': 5, '_': 6},  # From state 1, if input is a digit, '.', 'eE', or '_', stay in state 1
        2: {'digit': 4, '_': 6},                   # From state 2, if input is a digit or '_', transition to state 4 or 6
        3: {'digit': 4},                           # From state 3, if input is a digit, transition to state 4
        4: {'digit': 4, 'eE': 5, '_': 6},          # From state 4, if input is a digit, 'eE', or '_', stay in state 4
        5: {'sign': 6, 'digit': 7},                # From state 5, if input is a sign or digit, transition to state 6 or 7
        6: {'digit': 7},                           # From state 6, if input is a digit, transition to state 7
        7: {'digit': 7}                            # From state 7, if input is a digit, stay in state 7
    }
    state = 0
    for char in input_str:
        if state in {0, 1} and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        elif state in {0, 1} and char == '.':
            state = transitions.get(state, {}).get('.', -1)
        elif state == 1 and char.lower() in 'e':
            state = transitions.get(state, {}).get('eE', -1)
        elif state == 1 and char == '_':
            state = transitions.get(state, {}).get('_', -1)
        elif state == 2 and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        elif state == 3 and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        elif state == 3 and char == '_':
            state = transitions.get(state, {}).get('_', -1)
        elif state == 4 and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        elif state == 4 and char.lower() in 'e':
            state = transitions.get(state, {}).get('eE', -1)
        elif state == 4 and char == '_':
            state = transitions.get(state, {}).get('_', -1)
        elif state in {5, 6} and char in '+-':
            state = transitions.get(state, {}).get('sign', -1)
        elif state in {5, 6} and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        elif state == 7 and char.isdigit():
            state = transitions.get(state, {}).get('digit', -1)
        if state == -1:
            return False
    return state in {1, 4, 7, 3}

# Prompt user for input string
input_str = input("Enter a string to check if it's a valid floating-point integer: ")
print(f"{input_str}: {is_float(input_str)}")