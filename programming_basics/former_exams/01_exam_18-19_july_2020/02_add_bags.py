price_luggage_over_20 = float(input())
kg_luggage = float(input())
days_before_trip = int(input())
num_bags = int(input())
price = 0

if kg_luggage < 10:
    price = price_luggage_over_20 * 0.20
elif 10 <= kg_luggage <= 20:
    price = price_luggage_over_20 * 0.5
else:
    price = price_luggage_over_20
if days_before_trip > 30:
    price *= 1.10
elif 7 <= days_before_trip <= 30:
    price *= 1.15
elif days_before_trip < 7:
    price *= 1.40

total_price = price * num_bags
print(f"The total price of bags is: {total_price:.2f} lv.")
