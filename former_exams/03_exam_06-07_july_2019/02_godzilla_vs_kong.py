budget_movie = float(input())
number_statists = int(input())
price_equipment_per_person = float(input())

decor = budget_movie * 0.10
total_equipment_price = number_statists * price_equipment_per_person
if number_statists > 150:
    total_equipment_price *= 0.90
total = decor + total_equipment_price
difference = abs(budget_movie - total)

if budget_movie >= total:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
else:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
