def take_odd_command(f_password):
    converted_string = ""
    for index in range(1, len(f_password), 2):
        converted_string += f_password[index]
    f_password = converted_string
    print(f_password)
    return f_password


def cut_command(f_password, f_command):
    start_index = int(f_command[1])
    length = int(f_command[2])
    end_index = start_index + length
    substring = f_password[start_index:end_index]
    f_password = f_password.replace(substring, "", 1)
    print(f_password)
    return f_password


def substitute_command(f_password, f_command):
    substring = f_command[1]
    replacement = f_command[2]
    if substring in f_password:
        f_password = f_password.replace(substring, replacement)
        print(f_password)
    else:
        print("Nothing to replace!")
    return f_password


password = input()
command = input()

while not command == "Done":
    command = command.split()
    if command[0] == "TakeOdd":
        password = take_odd_command(password)
    elif command[0] == "Cut":
        password = cut_command(password, command)
    elif command[0] == "Substitute":
        password = substitute_command(password, command)
    command = input()

print(f"Your password is: {password}")
