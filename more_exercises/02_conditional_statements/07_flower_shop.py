import math
num_magnolias = int(input())
num_hyacinth = int(input())
num_roses = int(input())
num_cactus = int(input())
price_gift = float(input())

price_magnolias = 3.25 * num_magnolias
price_hyacinth = 4 * num_hyacinth
price_roses = 3.50 * num_roses
price_cactus = 8 * num_cactus

total_price = price_magnolias + price_hyacinth + price_roses + price_cactus
total_price *= 0.95
difference = abs(total_price - price_gift)

if total_price >= price_gift:
    print(f"She is left with {math.floor(difference)} leva.")
elif total_price < price_gift:
    print(f"She will have to borrow {math.ceil(difference)} leva.")
