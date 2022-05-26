import math

number_people = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

total_price_entrance_fee = number_people * entrance_fee
number_deck_chairs = math.ceil(number_people * 0.75)
number_umbrellas = math.ceil(number_people * 0.5)

total_price = total_price_entrance_fee + (number_deck_chairs * deck_chair_price) + (number_umbrellas * umbrella_price)

print(f"{total_price:.2f} lv." )
