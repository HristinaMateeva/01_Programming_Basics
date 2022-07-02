def rounding(input_data):
    result = []
    for el in input_data:
        current_rounded_num = round(float(el))
        result.append(current_rounded_num)
    return result


input_list = input().split()

print(rounding(input_list))
