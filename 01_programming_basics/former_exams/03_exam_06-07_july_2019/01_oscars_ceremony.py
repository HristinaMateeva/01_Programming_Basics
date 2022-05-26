rent_hall = int(input())

statue_price = rent_hall * 0.70
catering_price = statue_price * 0.85
sound_price = catering_price * 0.50

total = rent_hall + statue_price + catering_price + sound_price

print(f"{total:.2f}")
