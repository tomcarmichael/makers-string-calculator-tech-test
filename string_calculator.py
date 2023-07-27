def string_calculator(input_string):
    input_array = input_string.split(' ')

    if len(input_array) == 1:
        return [input_string, float(input_string)]
    else:
        result = float(input_array[0]) + float(input_array[2])
        return [input_string, result]