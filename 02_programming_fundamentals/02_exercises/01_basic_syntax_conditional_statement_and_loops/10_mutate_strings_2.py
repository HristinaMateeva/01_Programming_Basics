string_1 = input()
string_2 = input()

current_string = ""
previous_string = string_1

for iteration in range(len(string_1)):
    for index_str_2 in range(iteration + 1):
        current_string += string_2[index_str_2]
    for index_str_1 in range(iteration + 1, len(string_1)):
        current_string += string_1[index_str_1]
    if previous_string != current_string:
        print(current_string)
    # Prepare data for the next iteration
    previous_string = current_string
    current_string = ""
