command = input()

doubled_string = ""

while not command == "End":
    for symbol in range(len(command)):
        if command == "SoftUni":
            break
        else:
            doubled_string += command[symbol] * 2
    if doubled_string:
        print(doubled_string)
    doubled_string = ""

    command = input()
