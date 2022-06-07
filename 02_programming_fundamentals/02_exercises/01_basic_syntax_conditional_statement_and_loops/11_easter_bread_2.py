budget = float(input())
price_per_kg_flour = float(input())

price_pack_eggs = price_per_kg_flour * 0.75
price_milk_per_liter = price_per_kg_flour * 1.25
total_price_per_bread = price_pack_eggs + price_per_kg_flour + (price_milk_per_liter / 4)

count_bread = 0
count_eggs = 0

while budget >= total_price_per_bread:
    count_bread += 1
    count_eggs += 3
    budget -= total_price_per_bread
    if count_bread % 3 == 0:
        count_eggs -= count_bread - 2

print(f"You made {count_bread} loaves of Easter bread! Now you have {count_eggs} eggs and {budget:.2f}BGN left.")
