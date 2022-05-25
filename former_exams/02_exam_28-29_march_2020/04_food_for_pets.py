number_days = int(input())
total_quantity_food = float(input())

total_eaten_food = 0
eaten_food_dog = 0
eaten_food_cat = 0
total_eaten_biscuits_per_day = 0
total_biscuits = 0

for num in range(1, number_days + 1):
    food_per_day = 0
    quantity_eaten_food_dog = int(input())
    quantity_eaten_food_cat = int(input())
    eaten_food_dog += quantity_eaten_food_dog
    eaten_food_cat += quantity_eaten_food_cat
    if num % 3 == 0:
        food_per_day = quantity_eaten_food_dog + quantity_eaten_food_cat
        total_eaten_biscuits_per_day = food_per_day * 0.10
        total_biscuits += total_eaten_biscuits_per_day

total_eaten_food = eaten_food_dog + eaten_food_cat
percent_total_eaten_food = total_eaten_food / total_quantity_food * 100
percent_total_eaten_dog_food = eaten_food_dog / total_eaten_food * 100
percent_total_eaten_cat_food = eaten_food_cat / total_eaten_food * 100

print(f"Total eaten biscuits: {round(total_biscuits)}gr.")
print(f"{percent_total_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_total_eaten_dog_food:.2f}% eaten from the dog.")
print(f"{percent_total_eaten_cat_food:.2f}% eaten from the cat.")
