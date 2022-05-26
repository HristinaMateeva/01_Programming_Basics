purchased_quantity_food_kg = int(input())
command = input()

is_enough = True
eaten_food = 0
purchased_quantity_food_gr = purchased_quantity_food_kg * 1000

while command != "Adopted":
    quantity_food = int(command)
    eaten_food += quantity_food
    if eaten_food > purchased_quantity_food_gr:
        is_enough = False
    command = input()
difference = abs(purchased_quantity_food_gr - eaten_food)

if is_enough:
    print(f"Food is enough! Leftovers: {difference} grams." )
else:
    print(f"Food is not enough. You need {difference} grams more." )
