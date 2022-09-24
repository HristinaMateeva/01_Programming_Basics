def plant_validation(f_plant_data, f_current_data):
    f_plant = f_current_data[0]
    if f_plant in f_plant_data:
        return True
    else:
        print("error")
        return False


def rate_command(f_plant_data, f_current_data):
    f_plant = f_current_data[0]
    rating = int(f_current_data[1])
    f_plant_data[f_plant]["rating"].append(rating)
    return f_plant_data


def update_command(f_plant_data, f_current_data):
    f_plant = f_current_data[0]
    new_rarity = int(f_current_data[1])
    f_plant_data[f_plant]["rarity"] = new_rarity
    return f_plant_data


def reset_command(f_plant_data, f_current_data):
    f_plant = f_current_data[0]
    f_plant_data[f_plant]["rating"] = []
    return f_plant_data


number = int(input())

plant_data = {}

for num in range(number):
    initial_command = input().split("<->")
    plant = initial_command[0]
    rarity = int(initial_command[1])
    plant_data[plant] = {"rarity": rarity, "rating": [], "average_rating": 0}

command = input()

while not command == "Exhibition":
    command = command.split(": ")
    current_data = command[1].split(" - ")
    if plant_validation(plant_data, current_data):
        if command[0] == "Rate":
            plant_data = rate_command(plant_data, current_data)
        elif command[0] == "Update":
            plant_data = update_command(plant_data, current_data)
        elif command[0] == "Reset":
            plant_data = reset_command(plant_data, current_data)
    command = input()

for name_plant, statistics in plant_data.items():
    for statistic, value in statistics.items():
        if statistic == "rating":
            if value:
                plant_data[name_plant]["average_rating"] = sum(value) / len(value)

print("Plants for the exhibition:")

for plant_name, values in plant_data.items():
    print(f"- {plant_name}; Rarity: {plant_data[plant_name]['rarity']}; Rating: "
          f"{plant_data[plant_name]['average_rating']:.2f}")
