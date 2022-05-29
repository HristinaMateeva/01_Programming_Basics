joinery_number = int(input())
joinery_type = str(input())
delivery = str(input())

joinery_price = 0

if joinery_type == "90X130":
    joinery_price = 110
    if joinery_number > 60:
        joinery_price *= 0.92
    elif joinery_number > 30:
        joinery_price *= 0.95
elif joinery_type == "100X150":
    joinery_price = 140
    if joinery_number > 80:
        joinery_price *= 0.90
    elif joinery_price > 40:
        joinery_price *= 0.94
elif joinery_type == "130X180":
    joinery_price = 190
    if joinery_number > 50:
        joinery_price *= 0.88
    elif joinery_number > 20:
        joinery_price *= 0.93
elif joinery_type == "200X300":
    joinery_price = 250
    if joinery_number > 50:
        joinery_price *= 0.86
    elif joinery_number > 25:
        joinery_price *= 0.91
total_cost = joinery_price * joinery_number
if delivery == "With delivery":
    total_cost += 60
if joinery_number < 10:
    print("Invalid order")
elif joinery_number > 99:
    total_cost *= 0.96
    print(f"{total_cost:.2f} BGN")
else:
    print(f"{total_cost:.2f} BGN")