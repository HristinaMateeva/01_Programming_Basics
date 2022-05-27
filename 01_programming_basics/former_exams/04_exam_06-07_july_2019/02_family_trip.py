budget = float(input())
number_night_stand = float(input())
price_per_night = float(input())
additional_charges_percent = int(input())

if number_night_stand > 7:
    price_per_night *= 0.95

total_price_all_nights = number_night_stand * price_per_night
additional_charges_total = budget * (additional_charges_percent / 100)
total = total_price_all_nights + additional_charges_total
difference = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
