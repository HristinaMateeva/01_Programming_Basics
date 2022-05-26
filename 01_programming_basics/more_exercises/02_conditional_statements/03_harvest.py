import math

square_meters = int(input())
kg_grapes_per_square_meter = float(input())
needed_liters = int(input())
num_workers = int(input())

kg_for_liter = 2.5
total_kg_grapes = square_meters * kg_grapes_per_square_meter
wine = 0.4 * total_kg_grapes / 2.5
difference = abs(wine - needed_liters)
wine_for_workers = difference / num_workers

if wine < needed_liters:
    print(f"It will be a tough winter! More {math.floor(difference)} liters wine needed.")
elif wine >= needed_liters:
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.ceil(difference)} liters left -> {math.ceil(wine_for_workers)} liters per person.")
