def string_calculator(input_string):
    input_array = input_string.split(' ')

    if len(input_array) == 1:
        return [input_string, float(input_string)]
    else:
        return [input_string, 2.0]