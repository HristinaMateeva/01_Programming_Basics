def blacklist(friends, cmd, blacklisted):
    name = cmd[1]
    if name not in friends:
        print(f"{name} was not found.")
    else:
        index = friends.index(name)
        blacklisted.append(name)
        print(f"{name} was blacklisted.")
        friends[index] = "Blacklisted"
    return friends, blacklisted


def error(friends, cmd, lost):
    index = int(cmd[1])
    name = friends[index]
    if 0 <= index < len(friends) and name != "Blacklisted" and name != "Lost":
        lost.append(name)
        print(f"{name} was lost due to an error.")
        friends[index] = "Lost"
    return friends, lost


def change(friends, cmd):
    index = int(cmd[1])
    new_name = cmd[2]
    if 0 <= index < len(friends):
        old_name = friends[index]
        print(f"{old_name} changed his username to {new_name}.")
        friends[index] = new_name
    return friends


friends_list = input().split(", ")
command = input()

blacklisted_names = []
lost_names = []

while not command == "Report":
    command = command.split()
    if command[0] == "Blacklist":
        friends_list, blacklisted_names = blacklist(friends_list, command, blacklisted_names)
    elif command[0] == "Error":
        friends_list, lost_names = error(friends_list, command, lost_names)
    elif command[0] == "Change":
        friends_list = change(friends_list, command)
    command = input()

print(f"Blacklisted names: {len(blacklisted_names)}")
print(f"Lost names: {len(lost_names)}")
print(" ".join(friends_list))
