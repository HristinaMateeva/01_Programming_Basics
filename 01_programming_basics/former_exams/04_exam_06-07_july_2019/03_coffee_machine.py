drink_type = input()
sugar = input()
number_of_drinks = int(input())

total_price_drinks = 0

if drink_type == "Espresso":
    if sugar == "Without":
        total_price_drinks = number_of_drinks * 0.9 * 0.65
    elif sugar == "Normal":
        total_price_drinks = number_of_drinks * 1
    elif sugar == "Extra":
        total_price_drinks = number_of_drinks * 1.2
    if number_of_drinks >= 5:
        total_price_drinks *= 0.75
elif drink_type == "Cappuccino":
    if sugar == "Without":
        total_price_drinks = number_of_drinks * 1 * 0.65
    elif sugar == "Normal":
        total_price_drinks = number_of_drinks * 1.2
    elif sugar == "Extra":
        total_price_drinks = number_of_drinks * 1.6
elif drink_type == "Tea":
    if sugar == "Without":
        total_price_drinks = number_of_drinks * 0.5 * 0.65
    elif sugar == "Normal":
        total_price_drinks = number_of_drinks * 0.6
    elif sugar == "Extra":
        total_price_drinks = number_of_drinks * 0.7

if total_price_drinks > 15:
    total_price_drinks *= 0.8

print(f"You bought {number_of_drinks} cups of {drink_type} for {total_price_drinks:.2f} lv.")
