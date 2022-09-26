def insert_space_command(f_concealed_message, f_command):
    index = int(f_command[1])
    left_side = f_concealed_message[:index]
    right_side = f_concealed_message[index:]
    f_concealed_message = left_side + " " + right_side
    print(f_concealed_message)
    return f_concealed_message


def reverse_command(f_concealed_message, f_command):
    substring = f_command[1]
    if substring not in f_concealed_message:
        print("error")
    else:
        reversed_substring = substring[::-1]
        f_concealed_message = f_concealed_message.replace(substring, "", 1)
        f_concealed_message = f_concealed_message + reversed_substring
        print(f_concealed_message)
    return f_concealed_message


def change_all_command(f_concealed_message, f_command):
    substring = f_command[1]
    replacement = f_command[2]
    f_concealed_message = f_concealed_message.replace(substring, replacement)
    print(f_concealed_message)
    return f_concealed_message


concealed_message = input()

command = input()

while not command == "Reveal":
    command = command.split(":|:")
    if command[0] == "InsertSpace":
        concealed_message = insert_space_command(concealed_message, command)
    elif command[0] == "Reverse":
        concealed_message = reverse_command(concealed_message, command)
    elif command[0] == "ChangeAll":
        concealed_message = change_all_command(concealed_message, command)
    command = input()

print(f"You have a new text message: {concealed_message}")
