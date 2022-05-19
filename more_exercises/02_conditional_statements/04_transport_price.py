kilometers = int(input())
daytime = input()

price_day_taxi = 0.79
price_night_taxi = 0.90
price_bus = 0.09
price_train = 0.06
total_price = 0

if daytime == "day":
    if kilometers < 20:
        total_price = 0.70 + kilometers * price_day_taxi
    elif 20 <= kilometers < 100:
        total_price = kilometers * price_bus
    elif kilometers >= 100:
        total_price = kilometers * price_train
elif daytime == "night":
    if kilometers < 20:
        total_price = 0.70 + kilometers * price_night_taxi
    elif 20 <= kilometers < 100:
        total_price = kilometers * price_bus
    elif kilometers >= 100:
        total_price = kilometers * price_train

print(f"{total_price:.2f}")
