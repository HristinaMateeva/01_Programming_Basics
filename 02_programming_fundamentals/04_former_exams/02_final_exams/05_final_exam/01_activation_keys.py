def contains_command(f_activation_key, f_command):
    substring = f_command[1]
    if substring in f_activation_key:
        print(f"{f_activation_key} contains {substring}")
    else:
        print("Substring not found!")


def flip_command(f_activation_key, f_command):
    sensitivity = f_command[1]
    start_index = int(f_command[2])
    end_index = int(f_command[3])
    left_side = f_activation_key[:start_index]
    right_side = f_activation_key[end_index:]
    substring = ""
    if sensitivity == "Upper":
        substring = (f_activation_key[start_index: end_index]).upper()
    elif sensitivity == "Lower":
        substring = (f_activation_key[start_index: end_index]).lower()
    f_activation_key = left_side + substring + right_side
    print(f_activation_key)
    return f_activation_key


def slice_command(f_activation_key, f_command):
    start_index = int(f_command[1])
    end_index = int(f_command[2])
    left_side = f_activation_key[:start_index]
    right_side = f_activation_key[end_index:]
    f_activation_key = left_side + right_side
    print(f_activation_key)
    return f_activation_key


activation_key = input()
command = input()

while not command == "Generate":
    command = command.split(">>>")
    if command[0] == "Contains":
        contains_command(activation_key, command)
    elif command[0] == "Flip":
        activation_key = flip_command(activation_key, command)
    elif command[0] == "Slice":
        activation_key = slice_command(activation_key, command)
    command = input()

print(f"Your activation key is: {activation_key}")
