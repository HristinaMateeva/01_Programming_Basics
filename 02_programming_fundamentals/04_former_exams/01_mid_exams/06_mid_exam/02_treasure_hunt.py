initial_loot = input().split("|")
command = input()
total_treasure = 0
stolen_elements = []

while not command == "Yohoho!":
    command = command.split()
    operation = command[0]
    if operation == "Loot":
        current_loot = command[1:]
        for el in current_loot:
            if el not in initial_loot:
                initial_loot.insert(0, el)
    elif operation == "Drop":
        drop_index = int(command[1])
        drop_element = initial_loot[drop_index]
        if 0 <= drop_index < len(initial_loot):
            initial_loot.remove(drop_element)
            initial_loot.append(drop_element)
    elif operation == "Steal":
        count = int(command[1])
        if len(initial_loot) <= count:
            stolen_elements = initial_loot.copy()
            initial_loot = []
        else:
            stolen_elements = initial_loot[len(initial_loot) - count:]
            initial_loot = initial_loot[:len(initial_loot) - count]
    command = input()

print(", ".join(stolen_elements))
if not initial_loot:
    print("Failed treasure hunt.")
else:
    for element in initial_loot:
        total_treasure += len(element)
    average = total_treasure / len(initial_loot)
    print(f"Average treasure gain: {average:.2f} pirate credits.")

#Not ready yet