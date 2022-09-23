def add_command(f_deck_of_the_cards, f_command):
    add_card = f_command[1]
    if add_card in f_deck_of_the_cards:
        print("Card is already in the deck")
    else:
        f_deck_of_the_cards.append(add_card)
        print("Card successfully added")
    return f_deck_of_the_cards


def remove_command(f_deck_of_the_cards, f_command):
    remove_card = f_command[1]
    if remove_card not in f_deck_of_the_cards:
        print("Card not found")
    else:
        f_deck_of_the_cards.remove(remove_card)
        print("Card successfully removed")
    return f_deck_of_the_cards


def remove_at_command(f_deck_of_the_cards, f_command):
    remove_index = int(f_command[1])
    if 0 <= remove_index < len(f_deck_of_the_cards):
        remove_card = f_deck_of_the_cards[remove_index]
        f_deck_of_the_cards.remove(remove_card)
        print("Card successfully removed")
    else:
        print("Index out of range")
    return f_deck_of_the_cards


def insert_command(f_deck_of_the_cards, f_command):
    insert_index = int(f_command[1])
    insert_card = f_command[2]
    if insert_index < 0 or insert_index >= len(f_deck_of_the_cards):
        print("Index out of range")
    elif insert_card in f_deck_of_the_cards:
        print("Card is already added")
    else:
        f_deck_of_the_cards.insert(insert_index, insert_card)
        print("Card successfully added")
    return f_deck_of_the_cards


deck_of_the_cards = input().split(", ")
num_commands = int(input())

for num in range(1, num_commands + 1):
    command = input().split(", ")
    operation = command[0]
    if operation == "Add":
        deck_of_the_cards = add_command(deck_of_the_cards, command)
    elif operation == "Remove":
        deck_of_the_cards = remove_command(deck_of_the_cards, command)
    elif operation == "Remove At":
        deck_of_the_cards = remove_at_command(deck_of_the_cards, command)
    elif operation == "Insert":
        deck_of_the_cards = insert_command(deck_of_the_cards, command)

print(", ".join(deck_of_the_cards))
