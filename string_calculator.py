def string_calculator(input_string):
    if not type(input_string) is str:
          raise TypeError("Argument must be a string")

    result = 0.0

    if input_string == '':
        return [input_string, result]

    input_array = input_string.split(' ')

    if len(input_array) == 1:
        return [input_string, float(input_string)]
    
    first_term = float(input_array[0])
    second_term = float(input_array[2])

    if input_array[1] == '+':
        result = first_term + second_term
    elif input_array[1] == '-':
        result = first_term - second_term
    elif input_array[1] == '/':
        result = first_term / second_term
    else:
        result = first_term * second_term

    return [input_string, result]
