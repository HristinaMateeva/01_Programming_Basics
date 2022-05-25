minutes_per_day = int(input())
number_walkings_per_day = int(input())
consumed_calories = int(input())

burned_calories = number_walkings_per_day * minutes_per_day * 5
half_calories = consumed_calories / 2

if burned_calories >= half_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
