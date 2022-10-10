from collections import deque

quantity_water = int(input())
name = input()

people = deque()

while not name == "Start":
    people.append(name)
    name = input()

command = input()

while not command == "End":
    command = command.split()
    if command[0] == "refill":
        liters_to_refill = int(command[1])
        quantity_water += liters_to_refill
    else:
        liters = int(command[0])
        if liters <= quantity_water:
            print(f"{people.popleft()} got water")
            quantity_water -= liters
        else:
            print(f"{people.popleft()} must wait")
    command = input()

print(f"{quantity_water} liters left")
