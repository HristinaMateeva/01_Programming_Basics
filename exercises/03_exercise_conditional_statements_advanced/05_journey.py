budget = float(input())
season = input()
spent_money = 0
type_of_vacation = " "
destination = " "
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spent_money = budget * 0.3
        type_of_vacation = "Camp"
    elif season == "winter":
        spent_money = budget * 0.7
        type_of_vacation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spent_money = budget * 0.4
        type_of_vacation = "Camp"
    elif season == "winter":
        spent_money = budget * 0.8
        type_of_vacation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    spent_money = budget * 0.9
    type_of_vacation = "Hotel"

print(f"Somewhere in {destination}")
print(f"{type_of_vacation} - {spent_money:.2f}")
