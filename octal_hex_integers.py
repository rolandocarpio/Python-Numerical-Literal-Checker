# Task 2: Recognizing Octal and Hexadecimal Integer Literals

def is_octal(input_str):
    # Define transition table for octal integers
    transitions = {
        0: {'zero': 1,},                     # From state 0, if input is '0', transition to state 1
        1: {'o': 2},                         # From state 1, if input is 'o', transition to state 2
        2: {'octal_digit': 3, '_': 2},       # From state 2, if input is an octal digit, transition to state 3. Underscores are allowed and ignored, so stay in state 2.
        3: {'octal_digit': 3, '_': 3}        # From state 3, if input is an octal digit, stay in state 3. Underscores are allowed and ignored, so stay in state 3.
    }
    state = 0
    for char in input_str:
        # Update state based on current state and input character
        if state == 0 and char == '0':
            state = transitions.get(state, {}).get('zero', -1)
        elif state == 1 and char.lower() == 'o':
            state = transitions.get(state, {}).get('o', -1)
        elif state in {2, 3} and ((char.isdigit() and char < '8') or char == '_'):
            state = transitions.get(state, {}).get('octal_digit', -1)
        else:
            return False
        # If the transition is invalid (state == -1), return False
        if state == -1:
            return False
    # Return True if the final state is 3 (accepting state), otherwise return False
    return state == 3


def is_hexadecimal(input_str):
    # Define transition table for hexadecimal integers
    transitions = {
        0: {'zero': 1},                  # From state 0, if input is '0', transition to state 1
        1: {'x': 2},                     # From state 1, if input is 'x', transition to state 2
        2: {'hex_digit': 3, '_': 2},     # From state 2, if input is a hex digit, transition to state 3. Underscores are allowed and ignored, so stay in state 2.
        3: {'hex_digit': 3, '_': 3}      # From state 3, if input is a hex digit, stay in state 3. Underscores are allowed and ignored, so stay in state 3.
    }
    state = 0
    for char in input_str:
        # Update state based on current state and input character
        if state == 0 and char == '0':
            state = transitions.get(state, {}).get('zero', -1)
        elif state == 1 and char.lower() == 'x':
            state = transitions.get(state, {}).get('x', -1)
        elif state in {2, 3} and (char.isdigit() or char == '_' or char.lower() in 'abcdef'):
            state = transitions.get(state, {}).get('hex_digit', -1)
        else:
            return False
        # If the transition is invalid (state == -1), return False
        if state == -1:
            return False
    # Return True if the final state is 3 (accepting state), otherwise return False
    return state == 3

# Prompt user for input string
input_str = input("Enter a string to check if it's a valid octal or hexadecimal integer: ")
print(f"{input_str}: octal={is_octal(input_str)}, hexadecimal={is_hexadecimal(input_str)}")