def invalid_input(sequence, count):
    middle_sequence = len(sequence) // 2
    element_to_add = "-" + str(count) + "a"
    sequence.insert(middle_sequence, element_to_add)
    sequence.insert(middle_sequence, element_to_add)
    print("Invalid input! Adding additional elements to the board")
    return sequence


sequence_of_elements = input().split()
command = input()

counter = 0
is_the_game_won = False

while not command == "end":
    first_card_index, second_card_index = [int(idx) for idx in command.split()]
    element_value = sequence_of_elements[first_card_index]
    counter += 1
    if first_card_index == second_card_index:
        sequence_of_elements = invalid_input(sequence_of_elements, counter)
    elif first_card_index < 0 or first_card_index >= len(sequence_of_elements):
        sequence_of_elements = invalid_input(sequence_of_elements, counter)
    elif second_card_index < 0 or second_card_index >= len(sequence_of_elements):
        sequence_of_elements = invalid_input(sequence_of_elements, counter)
    elif sequence_of_elements[first_card_index] == sequence_of_elements[second_card_index]:
        print(f"Congrats! You have found matching elements - {element_value}!")
        sequence_of_elements.remove(element_value)
        sequence_of_elements.remove(element_value)
    elif sequence_of_elements[first_card_index] != sequence_of_elements[second_card_index]:
        print("Try again!")
    if not sequence_of_elements:
        is_the_game_won = True
        break

    command = input()

if not is_the_game_won:
    print("Sorry you lose :(")
    print(" ".join(sequence_of_elements))
else:
    print(f"You have won in {counter} turns!")
