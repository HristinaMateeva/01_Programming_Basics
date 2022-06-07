budget = float(input())
price_kg_flour = float(input())

eggs_price = price_kg_flour * 0.75
milk_liter_price = price_kg_flour * 1.25
quarter_milk_price = milk_liter_price / 4
price_loaf = eggs_price + price_kg_flour + quarter_milk_price
loaves_counter = 0
colored_eggs = 0

while budget >= price_loaf:
    loaves_counter += 1
    budget -= price_loaf
    colored_eggs += 3
    if loaves_counter % 3 == 0:
        colored_eggs -= loaves_counter - 2

print(f"You made {loaves_counter} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
