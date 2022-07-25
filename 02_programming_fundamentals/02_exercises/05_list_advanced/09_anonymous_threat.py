def merge(data, f_command):
    start_index = int(f_command[1])
    end_index = int(f_command[2])
    merged_result = ""
    if start_index < 0:
        range_data = data[:end_index + 1]
    elif end_index >= len(data):
        range_data = data[start_index:]
    else:
        range_data = data[start_index:end_index + 1]
    for element in range_data:
        merged_result += element
    current_result = data[:start_index] + [merged_result] + data[end_index + 1:]
    return current_result


def divide(data, f_command):
    index = int(f_command[1])
    partitions = int(f_command[2])
    word = data[index]
    part_length = len(word) // partitions
    current_element = ""
    divided_list = []
    for ind in range(len(word)):
        if ind % part_length == 0 and ind != 0:
            divided_list.append(current_element)
            current_element = ""
            current_element += word[ind]
        else:
            current_element += word[ind]
    divided_list.append(current_element)
    if not len(word) % partitions == 0:
        last_element = divided_list[-2] + divided_list[-1]
        divided_list.pop(-1)
        divided_list.pop(-2)
        divided_list.append(last_element)
    data.pop(index)
    current_result = data[:index] + divided_list + data[index:]
    return current_result


input_line = input().split()
command = input()
current_list = input_line.copy()

while not command == "3:1":
    command = command.split()
    operation = command[0]
    if operation == "merge":
        current_list = merge(current_list, command)
    else:
        current_list = divide(current_list, command)
    command = input()

print(" ".join(current_list))

# Не е довършена