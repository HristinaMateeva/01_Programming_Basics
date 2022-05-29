desired_income = float(input())
command = input()
total_price = 0

while command != "Party!":
    cocktail_name = command
    number_cocktails = int(input())
    price_cocktail = len(cocktail_name) * number_cocktails
    if price_cocktail % 2 == 1:
        price_cocktail *= 0.75
    total_price += price_cocktail
    if total_price >= desired_income:
        break
    command = input()

difference = abs(total_price - desired_income)

if total_price >= desired_income:
    print("Target acquired.")
else:
    print(f"We need {difference:.2f} leva more.")
print(f"Club income - {total_price:.2f} leva.")
