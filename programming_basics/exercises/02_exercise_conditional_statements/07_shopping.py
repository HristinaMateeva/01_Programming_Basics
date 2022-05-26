budget = float(input())
number_video_cards = int(input())
number_processors = int(input())
number_ram = int(input())
video_cards_price = number_video_cards * 250
processor_price = video_cards_price * 0.35 * number_processors
ram_price = video_cards_price * 0.10 * number_ram
total = video_cards_price + processor_price + ram_price
if number_video_cards > number_processors:
    total = total * 0.85
difference = abs(budget - total)
if budget >= total:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
    