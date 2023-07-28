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
    
    try:
        first_term = float(input_array[0])
    except(ValueError):
        raise MathError()

    if len(input_array) == 1:
        return [input_string, first_term]
    
    try:
        second_term = float(input_array[2])
    except(ValueError):
        raise MathError()

    match input_array[1]:
        case '+':
            result = first_term + second_term
        case '-':
            result = first_term - second_term
        case '/':
            result = first_term / second_term
        case '*':
            result = first_term * second_term
        case _:
            raise MathError()

    return [input_string, result]
