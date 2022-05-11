days = int(input())
type_of_room = input()
rating = input()
night = days - 1
price_per_night = 0
if type_of_room == "room for one person":
    price_per_night = 18
elif type_of_room == "apartment":
    price_per_night = 25
    if days < 10:
        price_per_night *= 0.7
    elif days >= 10 and days <= 15:
        price_per_night *= 0.65
    elif days > 15:
        price_per_night *= 0.5
elif type_of_room == "president apartment":
    price_per_night = 35
    if days < 10:
        price_per_night *= 0.9
    elif days >= 10 and days <= 15:
        price_per_night *= 0.85
    elif days > 15:
        price_per_night *= 0.8
total = price_per_night * night
if rating == "positive":
    total *= 1.25
elif rating == "negative":
    total *= 0.9
print(f"{total:.2f}")
