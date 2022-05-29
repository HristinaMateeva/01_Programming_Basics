number_people = int(input())
number_nights = int(input())
number_cards = int(input())
number_tickets = int(input())

nights_total = number_nights * 20
cards_total = number_cards * 1.60
total_tickets = number_tickets * 6
total_per_person = nights_total + cards_total + total_tickets
total = total_per_person * number_people
final_price = total * 1.25

print(f"{final_price:.2f}")
