class MathError(Exception):
    def __init__(self):
        super().__init__("Input should be a valid mathematical sum separated by spaces")


def string_calculator(input_string):
    if not type(input_string) is str:
        raise TypeError("Argument must be a string")

    result = 0.0

    if input_string == '':
        return [input_string, result]

    input_array = input_string.split(' ')

    # Convert the first term to a float
    try:
        first_term = float(input_array[0])
    except(ValueError):
        raise MathError()
    
    # If only 1 number was provided
    if len(input_array) == 1:
        return [input_string, first_term]
    
    # Convert the second term to a float
    try:
        second_term = float(input_array[2])
    except(ValueError):
        raise MathError()
    
    # Check if they provided more than two terms
    if len(input_array) > 4:
        raise Exception('Maximum of two terms allowed in the sum')

    match input_array[1]:
        case '+':
            result = first_term + second_term
        case '-':
            result = first_term - second_term
        case '/':
            result = first_term / second_term
        case '*':
            result = first_term * second_term
        # Throw error if a valid operator was not provided
        case _:
            raise MathError()

    return [input_string, result]
