command = input()

meal_collection = {}
unliked_meals_counter = 0

while not command == "Stop":
    command = command.split("-")
    guest = command[1]
    meal = command[2]
    if command[0] == "Like":
        if guest not in meal_collection:
            meal_collection[guest] = []
            meal_collection[guest].append(meal)
        elif meal not in meal_collection[guest]:
            meal_collection[guest].append(meal)
    elif command[0] == "Dislike":
        if guest not in meal_collection:
            print(f"{guest} is not at the party.")
        elif meal not in meal_collection[guest]:
            print(f"{guest} doesn't have the {meal} in his/her collection.")
        else:
            meal_collection[guest].remove(meal)
            unliked_meals_counter += 1
            print(f"{guest} doesn't like the {meal}.")
    command = input()

for name, meals in meal_collection.items():
    print(f"{name}: {', '.join(meals)}")
print(f"Unliked meals: {unliked_meals_counter}")
