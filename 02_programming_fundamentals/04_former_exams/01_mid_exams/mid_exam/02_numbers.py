def add_command(f_sequence_of_numbers, f_command):
    add_value = int(f_command[1])
    f_sequence_of_numbers.append(add_value)
    return f_sequence_of_numbers


def remove_command(f_sequence_of_numbers, f_command):
    remove_value = int(f_command[1])
    if remove_value in f_sequence_of_numbers:
        f_sequence_of_numbers.remove(remove_value)
    return f_sequence_of_numbers


def replace_command(f_sequence_of_numbers, f_command):
    replace_value = int(f_command[1])
    replacement_value = int(f_command[2])
    if replace_value in f_sequence_of_numbers:
        replace_index = f_sequence_of_numbers.index(replace_value)
        f_sequence_of_numbers[replace_index] = replacement_value
    return f_sequence_of_numbers


def collapse_command(f_sequence_of_numbers, f_command):
    collapse_value = int(f_command[1])
    collapsed_list = []
    for el in f_sequence_of_numbers:
        if el >= collapse_value:
            collapsed_list.append(el)
    return collapsed_list


sequence_of_numbers = [int(el) for el in input().split()]
command = input()

while not command == "Finish":
    command = command.split()
    operation = command[0]
    if operation == "Add":
        sequence_of_numbers = add_command(sequence_of_numbers, command)
    elif operation == "Remove":
        sequence_of_numbers = remove_command(sequence_of_numbers, command)
    elif operation == "Replace":
        sequence_of_numbers = replace_command(sequence_of_numbers, command)
    elif operation == "Collapse":
        sequence_of_numbers = collapse_command(sequence_of_numbers, command)
    command = input()

sequence_of_numbers = [str(element) for element in sequence_of_numbers]
print(" ".join(sequence_of_numbers))
