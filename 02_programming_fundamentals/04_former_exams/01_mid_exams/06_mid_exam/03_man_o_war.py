pirate_ship = [int(el) for el in input().split(">")]
warship = [int(el) for el in input().split(">")]
max_health = int(input())
command = input()

while not command == "Retire":
    command = command.split()
    operation = command[0]
    if operation == "Fire":
        fire_index = int(command[1])
        fire_damage = int(command[2])
        if 0 <= fire_index < len(warship):
            warship[fire_index] -= fire_damage
            if warship[fire_index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
    elif operation == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        defend_damage = int(command[3])
        if 0 <= start_index < len(pirate_ship) and 0 <= end_index < len(pirate_ship):
            for index in range(start_index, end_index + 1):
                pirate_ship[index] -= defend_damage
                if pirate_ship[index] <= 0:
                    print('You lost! The pirate ship has sunken.')
                    exit()
    elif operation == "Repair":
        repair_index = int(command[1])
        health = int(command[2])
        if 0 <= repair_index < len(pirate_ship):
            if 0 <= repair_index < len(pirate_ship):
                if pirate_ship[repair_index] + health >= max_health:
                    pirate_ship[repair_index] = max_health
                else:
                    pirate_ship[repair_index] += health
    elif operation == "Status":
        below_limit = max_health * 0.2
        counter = 0
        for item in pirate_ship:
            if item < below_limit:
                counter += 1
        print(f"{counter} sections need repair.")
    command = input()

pirates_ship_sum = sum(pirate_ship)
warship_sum = sum(warship)
print(f"Pirate ship status: {pirates_ship_sum}")
print(f"Warship status: {warship_sum}")
