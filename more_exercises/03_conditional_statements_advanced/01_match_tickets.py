budget = float(input())
category = input()
num_people = int(input())
price_tickets = 0
left_fee = 0

if 1 <= num_people <= 4:
    left_fee = budget * 0.25
    if category == "Normal":
        price_tickets = num_people * 249.99
    elif category == "VIP":
        price_tickets = num_people * 499.99
elif 5 <= num_people <= 9:
    left_fee = budget * 0.40
    if category == "Normal":
        price_tickets = num_people * 249.99
    elif category == "VIP":
        price_tickets = num_people * 499.99
elif 10 <= num_people <= 24:
    left_fee = budget * 0.50
    if category == "Normal":
        price_tickets = num_people * 249.99
    elif category == "VIP":
        price_tickets = num_people * 499.99
elif 25 <= num_people <= 49:
    left_fee = budget * 0.60
    if category == "Normal":
        price_tickets = num_people * 249.99
    elif category == "VIP":
        price_tickets = num_people * 499.99
elif num_people >= 50:
    left_fee = budget * 0.75
    if category == "Normal":
        price_tickets = num_people * 249.99
    elif category == "VIP":
        price_tickets = num_people * 499.99

difference = abs(left_fee - price_tickets)

if left_fee >= price_tickets:
    print(f"Yes! You have {difference:.2f} leva left.")
elif left_fee < price_tickets:
    print(f"Not enough money! You need {difference:.2f} leva.")
