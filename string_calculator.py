def string_calculator(input_string):
    if not type(input_string) is str:
        raise TypeError("Argument must be a string")

    result = 0.0

    if input_string == '':
        return [input_string, result]

    input_array = input_string.split(' ')

    if len(input_array) == 1:
        return [input_string, float(input_string)]
    
    try:
        first_term = float(input_array[0])
        second_term = float(input_array[2])
    except(ValueError):
        raise Exception("Input should be a valid mathematical sum separated by spaces")


    if input_array[1] == '+':
        result = first_term + second_term
    elif input_array[1] == '-':
        result = first_term - second_term
    elif input_array[1] == '/':
        result = first_term / second_term
    elif input_array[1] == '*':
        result = first_term * second_term
    else:
        raise Exception("Input should be a valid mathematical sum separated by spaces")

    return [input_string, result]
