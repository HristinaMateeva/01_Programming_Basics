def check_card_exist(items_list, item):
    if item in items_list:
        return True
    return False


def remove_at_index(items_list, items_data):
    current_index = int(items_data)
    if 0 <= current_index < len(items_list):
        card = items_list[current_index]
        items_list.remove(card)
        print("Card successfully removed")
    else:
        print("Index out of range")
    return items_list


list_of_cards = input().split(", ")
command_data = int(input())

for num_of_command in range(command_data):
    command = input().split(", ")
    card_or_index = command[1]
    if command[0] == "Add":
        if not check_card_exist(list_of_cards, card_or_index):
            list_of_cards.append(card_or_index)
            print("Card successfully added")
        else:
            print("Card is already in the deck")
    elif command[0] == "Remove":
        if check_card_exist(list_of_cards, card_or_index):
            list_of_cards.remove(card_or_index)
            print("Card successfully removed")
        else:
            print("Card not found")
    elif command[0] == "Remove At":
        list_of_cards = remove_at_index(list_of_cards, card_or_index)
    elif command[0] == "Insert":
        index = int(command[1])
        new_card = command[2]
        if index < 0 or index >= len(list_of_cards):
            print("Index out of range")
        elif check_card_exist(list_of_cards, new_card):
            print("Card is already added")
        else:
            list_of_cards.insert(index, new_card)
            print("Card successfully added")

print(", ".join(list_of_cards))
