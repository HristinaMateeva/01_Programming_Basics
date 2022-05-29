percent_fat = int(input())
percent_protein = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

gram_fat = 9
gram_protein = 4
gram_carbohydrates = 4

total_fat = total_calories * (percent_fat / 100) / 9
total_proteins = total_calories * (percent_protein / 100) / 4
total_carbohydrates = total_calories * (percent_carbohydrates / 100) / 4
total_food = total_fat + total_proteins + total_carbohydrates
calories = total_calories / total_food
calories_without_water = calories * (100 - percent_water) / 100

print(f"{calories_without_water:.4f}")
