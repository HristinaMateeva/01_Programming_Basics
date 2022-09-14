def shoot_command(f_sequence, f_command):
    shoot_index = int(f_command[1])
    shoot_power = int(f_command[2])
    if 0 <= shoot_index < len(f_sequence):
        f_sequence[shoot_index] -= shoot_power
        if f_sequence[shoot_index] <= 0:
            f_sequence.pop(shoot_index)
    return f_sequence


def add_command(f_sequence, f_command):
    add_index = int(f_command[1])
    add_value = int(f_command[2])
    if 0 <= add_index < len(f_sequence):
        f_sequence.insert(add_index, add_value)
    else:
        print("Invalid placement!")
    return f_sequence


def strike_command(f_sequence, f_command):
    strike_index = int(f_command[1])
    strike_radius = int(f_command[2])
    left_index = strike_index - strike_radius
    right_index = strike_index + strike_radius
    if left_index >= 0 and right_index < len(f_sequence):
        left_part = f_sequence[:left_index]
        right_part = f_sequence[right_index + 1:]
        f_sequence = left_part + right_part
    else:
        print("Strike missed!")
    return f_sequence


sequence_of_targets = [int(el) for el in input().split()]
command = input()

while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        sequence_of_targets = shoot_command(sequence_of_targets, command)
    elif command[0] == "Add":
        sequence_of_targets = add_command(sequence_of_targets, command)
    elif command[0] == "Strike":
        sequence_of_targets = strike_command(sequence_of_targets,command)
    command = input()

sequence_of_targets = [str(el) for el in sequence_of_targets]
print("|".join(sequence_of_targets))
