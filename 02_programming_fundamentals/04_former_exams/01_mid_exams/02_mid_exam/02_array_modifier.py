def swap_command(sequence, f_operation):
    index_1 = int(f_operation[1])
    index_2 = int(f_operation[2])
    sequence[index_1], sequence[index_2] = sequence[index_2], sequence[index_1]
    return sequence


def multiply_command(sequence, f_operation):
    index_1 = int(f_operation[1])
    index_2 = int(f_operation[2])
    changed_element_value = sequence[index_1] * sequence[index_2]
    sequence[index_1] = changed_element_value
    return sequence


def decrease_command(sequence):
    sequence = [(element - 1) for element in sequence]
    return sequence


sequence_of_integers = [int(el) for el in input().split()]
command = input()

while not command == "end":
    operation = command.split()
    if operation[0] == "swap":
        sequence_of_integers = swap_command(sequence_of_integers, operation)
    elif operation[0] == "multiply":
        sequence_of_integers = multiply_command(sequence_of_integers, operation)
    elif operation[0] == "decrease":
        sequence_of_integers = decrease_command(sequence_of_integers)
    command = input()

sequence_of_strings = [str(element) for element in sequence_of_integers]
print(", ".join(sequence_of_strings))
