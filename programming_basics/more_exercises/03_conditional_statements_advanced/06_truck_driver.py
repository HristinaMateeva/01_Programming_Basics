season = input()
km_per_month = float(input())
wage = 0
if km_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        wage = km_per_month * 0.75 * 4
    elif season == "Summer":
        wage = km_per_month * 0.90 * 4
    elif season == "Winter":
        wage = km_per_month * 1.05 * 4
elif 5000 < km_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        wage = km_per_month * 0.95 * 4
    elif season == "Summer":
        wage = km_per_month * 1.10 * 4
    elif season == "Winter":
        wage = km_per_month * 1.25 * 4
elif 10000 < km_per_month <= 20000:
    wage = km_per_month * 1.45 * 4

wage *= 0.90
print(f"{wage:.2f}")
