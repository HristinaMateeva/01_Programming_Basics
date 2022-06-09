animal_list = input().split(", ")

if animal_list[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    animal_position = len(animal_list) - animal_list.index("wolf") - 1
    print(f"Oi! Sheep number {animal_position}! You are about to be eaten by a wolf!")
