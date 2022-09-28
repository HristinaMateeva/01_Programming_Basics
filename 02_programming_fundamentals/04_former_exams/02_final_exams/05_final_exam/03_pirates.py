def plunder_command(f_target_data, f_command):
    town = f_command[1]
    people = int(f_command[2])
    gold = int(f_command[3])
    f_target_data[town]["population"] -= people
    f_target_data[town]["gold"] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if f_target_data[town]["population"] <= 0 or f_target_data[town]["gold"] <= 0:
        print(f"{town} has been wiped off the map!")
        del f_target_data[town]
    return f_target_data


def prosper_command(f_target_data, f_command):
    town = f_command[1]
    gold = int(f_command[2])
    if gold < 0:
        print("Gold added cannot be a negative number!")
    else:
        f_target_data[town]["gold"] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {f_target_data[town]['gold']} gold.")
    return f_target_data


initial_command = input()

target_data = {}

while not initial_command == "Sail":
    initial_command = initial_command.split("||")
    target_city = initial_command[0]
    target_city_population = int(initial_command[1])
    target_city_gold = int(initial_command[2])
    if target_city not in target_data:
        target_data[target_city] = {"population": target_city_population, "gold": target_city_gold}
    else:
        target_data[target_city]["population"] += target_city_population
        target_data[target_city]["gold"] += target_city_gold
    initial_command = input()

command = input()

while not command == "End":
    command = command.split("=>")
    if command[0] == "Plunder":
        target_data = plunder_command(target_data, command)
    elif command[0] == "Prosper":
        target_data = prosper_command(target_data, command)
    command = input()

if target_data:
    print(f"Ahoy, Captain! There are {len(target_data)} wealthy settlements to go to:")
    for city, data in target_data.items():
        print(f"{city} -> Population: {target_data[city]['population']} citizens, Gold: {target_data[city]['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
