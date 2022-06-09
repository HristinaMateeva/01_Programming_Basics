input_string = input()

result_list = []

for index in range(len(input_string)):
    if input_string[index].isupper():
        result_list.append(index)

print(result_list)
