dancers = int(input())
points = float(input())
season = input()
place = input()

total_price = 0

if place == "Bulgaria":
    if season == "summer":
        total_price = points * dancers
        total_price *= 0.95
    elif season == "winter":
        total_price = points * dancers
        total_price *= 0.92
elif place == "Abroad":
    if season == "summer":
        total_price = (points * dancers) * 1.5
        total_price *= 0.90
    elif season == "winter":
        total_price = (points * dancers) * 1.5
        total_price *= 0.85

sum_after_charity = total_price * 0.25
sum_charity = total_price * 0.75
sum_per_person = sum_after_charity / dancers

print(f"Charity - {sum_charity:.2f}")
print(f"Money per dancer - {sum_per_person:.2f}")
