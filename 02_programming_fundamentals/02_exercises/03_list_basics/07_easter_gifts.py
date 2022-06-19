received_gifts = input().split()
command = input()

result_list = []

while not command == "No Money":
    possible_commands_list = command.split()
    received_command = possible_commands_list[0]
    type_of_gift = possible_commands_list[1]
    if received_command == "OutOfStock":
        for element in received_gifts:
            if type_of_gift in received_gifts:
                searched_index = received_gifts.index(possible_commands_list[1])
                received_gifts[searched_index] = "None"
            else:
                break
    elif received_command == "Required":
        if (len(received_gifts) - 1) >= int(possible_commands_list[2]) >= 0:
            searched_index = int(possible_commands_list[2])
            received_gifts[searched_index] = type_of_gift
    elif received_command == "JustInCase":
        received_gifts[-1] = type_of_gift
    command = input()

for el in received_gifts:
    if "None" in received_gifts:
        received_gifts.remove("None")
    else:
        break

print(" ".join(received_gifts))
