price_mackerel_kg = float(input())
price_toy_kg = float(input())
bonito_kg = float(input())
horse_mackerel_kg = float(input())
mussels_kg = float(input())
price_bonito_kg = price_mackerel_kg * 1.60
price_horse_mackerel_kg = price_toy_kg * 1.80
price_mussels = 7.50
total = bonito_kg * price_bonito_kg + horse_mackerel_kg * price_horse_mackerel_kg + mussels_kg * price_mussels
print(f"{total:.2f}")
