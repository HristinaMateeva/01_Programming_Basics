trip_price = float(input())
number_puzzles = int(input())
number_talking_dolls = int(input())
number_teddy_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
puzzle_price = number_puzzles * 2.60
talking_dolls_price = number_talking_dolls * 3
teddy_bear_price = number_teddy_bears * 4.10
minion_price = number_minions * 8.20
trucks_price = number_trucks * 2
total_numbers = number_puzzles + number_talking_dolls + number_teddy_bears + number_trucks + number_minions
total_sum = puzzle_price + talking_dolls_price + teddy_bear_price + minion_price + trucks_price
if total_numbers >= 50:
    total_sum = total_sum * 0.75
rent = total_sum * 0.10
total = total_sum - rent
difference = abs(total - trip_price)
if total >= trip_price:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
