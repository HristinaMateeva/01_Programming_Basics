type_fuel = input()
liters_fuel = float(input())
discount_card = input()

price_gas_per_liter = 0.93
price_diesel_per_liter = 2.33
price_gasoline_per_liter = 2.22
total_price = 0

if type_fuel == "Gas":
    if discount_card == "Yes":
        total_price = liters_fuel * (price_gas_per_liter - 0.08)
    elif discount_card == "No":
        total_price = liters_fuel * price_gas_per_liter
elif type_fuel == "Gasoline":
    if discount_card == "Yes":
        total_price = liters_fuel * (price_gasoline_per_liter - 0.18)
    elif discount_card == "No":
        total_price = liters_fuel * price_gasoline_per_liter
elif type_fuel == "Diesel":
    if discount_card == "Yes":
        total_price = liters_fuel * (price_diesel_per_liter - 0.12)
    elif discount_card == "No":
        total_price = liters_fuel * price_diesel_per_liter

if liters_fuel >= 20 and liters_fuel <= 25:
    total_price *= 0.92
elif liters_fuel > 25:
    total_price *= 0.90
print(f"{total_price:.2f} lv.")
