food_grams = float(input()) * 1000
hay_grams = float(input()) * 1000
cover_grams = float(input()) * 1000
weight_grams = float(input()) * 1000

day = 1
is_enough = True

while day <= 30:
    if food_grams <= 300 or hay_grams <= 0 or cover_grams <= 0:
        is_enough = False
        break
    food_grams -= 300
    if day % 2 == 0:
        hay_grams -= food_grams * 0.05
    if day % 3 == 0:
        cover_grams -= weight_grams / 3
    day += 1

if not is_enough:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {(food_grams/1000):.2f}, Hay: {(hay_grams/1000):.2f}, Cover: {(cover_grams/1000):.2f}.")
