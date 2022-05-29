type_fruit = input()
size_set = input()
number_sets = int(input())

price_watermelon = 0
price_mango = 0
price_pineapple = 0
price_raspberry = 0
total_price = 0

if type_fruit == "Watermelon":
    if size_set == "small":
        price_watermelon = 2 * 56 * number_sets
        total_price += price_watermelon
    elif size_set == "big":
        price_watermelon = 5 * 28.70 * number_sets
        total_price += price_watermelon
elif type_fruit == "Mango":
    if size_set == "small":
        price_mango = 2 * 36.66 * number_sets
        total_price += price_mango
    elif size_set == "big":
        price_mango = 5 * 19.60 * number_sets
        total_price += price_mango
elif type_fruit == "Pineapple":
    if size_set == "small":
        price_pineapple = 2 * 42.10 * number_sets
        total_price += price_pineapple
    elif size_set == "big":
        price_pineapple = 5 * 24.80 * number_sets
        total_price += price_pineapple
elif type_fruit == "Raspberry":
    if size_set == "small":
        price_raspberry = 2 * 20 * number_sets
        total_price += price_raspberry
    elif size_set == "big":
        price_raspberry = 5 * 15.20 * number_sets
        total_price += price_raspberry

if 400 <= total_price <= 1000:
    total_price *= 0.85
elif total_price > 1000:
    total_price *= 0.5

print(f"{total_price:.2f} lv.")
