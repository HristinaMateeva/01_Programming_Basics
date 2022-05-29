airline = input()
num_tickets_adults = int(input())
num_tickets_kids = int(input())
net_price_adult_ticket = float(input())
fee_service = float(input())

net_price_kid_ticket = net_price_adult_ticket * 0.30
gross_price_adult_ticket = net_price_adult_ticket + fee_service
gross_price_kid_ticket = net_price_kid_ticket + fee_service
total = num_tickets_adults * gross_price_adult_ticket + num_tickets_kids * gross_price_kid_ticket
total_income = total * 0.2

print(f"The profit of your agency from {airline} tickets is {total_income:.2f} lv.")
