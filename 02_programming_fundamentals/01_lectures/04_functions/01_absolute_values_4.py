def absolute_values(string):
    input_list = input_string.split()
    result_list = []
    for item in input_list:
        item = abs(float(item))
        result_list.append(item)
    return result_list


input_string = input()

print(absolute_values(input_string))
