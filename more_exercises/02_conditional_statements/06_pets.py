import math

days = int(input())
left_food = int(input())
dog_food_per_day_kg = float(input())
cat_food_per_day_kg = float(input())
turtle_food_per_day_grams = float(input())

turtle_food_per_day_kg = turtle_food_per_day_grams / 1000
total_food_kg = days * (dog_food_per_day_kg + cat_food_per_day_kg + turtle_food_per_day_kg)
difference = abs(left_food - total_food_kg)

if left_food >= total_food_kg:
    print(f"{math.floor(difference)} kilos of food left.")
elif left_food < total_food_kg:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
