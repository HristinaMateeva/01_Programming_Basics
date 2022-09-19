def collect_command(f_items_list, f_command):
    item = f_command[1]
    if item not in f_items_list:
        f_items_list.append(item)
    return f_items_list


def drop_command(f_items_list, f_command):
    item = f_command[1]
    if item in f_items_list:
        f_items_list.remove(item)
    return f_items_list


def combine_items_command(f_items_list, f_command):
    old_item, new_item = (f_command[1]).split(":")
    if old_item in f_items_list:
        index = f_items_list.index(old_item)
        f_items_list.insert(index + 1, new_item)
    return f_items_list


def renew_command(f_items_list, f_command):
    item = f_command[1]
    if item in f_items_list:
        f_items_list.remove(item)
        f_items_list.append(item)
    return f_items_list


items_list = input().split(", ")
command = input()

while not command == "Craft!":
    command = command.split(" - ")
    if command[0] == "Collect":
        items_list = collect_command(items_list, command)
    elif command[0] == "Drop":
        items_list = drop_command(items_list, command)
    elif command[0] == "Combine Items":
        items_list = combine_items_command(items_list, command)
    elif command[0] == "Renew":
        items_list = renew_command(items_list, command)
    command = input()

print(", ".join(items_list))
