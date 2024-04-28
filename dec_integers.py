def is_decimal_integer(input_str):
    # Define transition table: state -> {input_char: next_state}
    transitions = {
        0: {'digit': 1, '_': 0},
        1: {'digit': 1, '_': 1}
    }
    state = 0
    # Iterate over each character in the input string
    for char in input_str:
        if char.isdigit() or char == '_':  # Check if the character is a digit or underscore
            state = transitions.get(state, {}).get('digit', -1)
        else:
            return False  # If a non-digit character (excluding underscores) is encountered, return False
        # If the transition is invalid (state == -1), return False
        if state == -1:
            return False
    # Return True if the final state is 1 (accepting state), otherwise return False
    return state == 1

# Prompt user for input string for Task 1
input_str = input("Enter a string to check if it's a valid decimal integer: ")
print(f"{input_str}: {is_decimal_integer(input_str)}")