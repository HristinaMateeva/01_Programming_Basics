def urgent_command(f_groceries_list, f_command):
    item = f_command[1]
    if item not in f_groceries_list:
        f_groceries_list.insert(0, item)
    return f_groceries_list


def unnecessary_command(f_groceries_list, f_command):
    item = f_command[1]
    if item in f_groceries_list:
        f_groceries_list.remove(item)
    return f_groceries_list


def correct_command(f_groceries_list, f_command):
    old_item = f_command[1]
    new_item = f_command[2]
    if old_item in f_groceries_list:
        index = f_groceries_list.index(old_item)
        groceries_list[index] = new_item
    return f_groceries_list


def rearrange_command(f_groceries_list, f_command):
    item = f_command[1]
    if item in f_groceries_list:
        f_groceries_list.remove(item)
        f_groceries_list.append(item)
    return f_groceries_list


groceries_list = input().split("!")
command = input()

while not command == "Go Shopping!":
    command = command.split()
    type_command = command[0]
    if type_command == "Urgent":
        groceries_list = urgent_command(groceries_list, command)
    elif type_command == "Unnecessary":
        groceries_list = unnecessary_command(groceries_list, command)
    elif type_command == "Correct":
        groceries_list = correct_command(groceries_list, command)
    elif type_command == "Rearrange":
        groceries_list = rearrange_command(groceries_list, command)
    command = input()

print(", ".join(groceries_list))
