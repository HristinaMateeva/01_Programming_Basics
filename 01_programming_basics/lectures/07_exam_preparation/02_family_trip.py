budget = float(input())
number_nights = int(input())
price_per_night = float(input())
percent_additional_expenses = int(input())

if number_nights > 7:
    price_per_night *= 0.95

all_nights_sum = number_nights * price_per_night
expenses = budget * (percent_additional_expenses / 100)
total = all_nights_sum + expenses
difference = abs(budget - total)

if budget >= total:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
