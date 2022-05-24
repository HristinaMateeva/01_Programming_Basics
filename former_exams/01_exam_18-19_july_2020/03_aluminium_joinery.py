num_joinery = int(input())
type_joinery = input()
receiving_way = input()
price = 0

if type_joinery == "90X130":
    price = 110
    if num_joinery > 60:
        price *= 0.92
    elif num_joinery > 30:
        price *= 0.95
elif type_joinery == "100X150":
    price = 140
    if num_joinery > 80:
        price *= 0.90
    elif num_joinery > 40:
        price *= 0.94
elif type_joinery == "130X180":
    price = 190
    if num_joinery > 50:
        price *= 0.88
    elif num_joinery > 20:
        price *= 0.93
elif type_joinery == "200X300":
    price = 250
    if num_joinery > 50:
        price *= 0.86
    elif num_joinery > 25:
        price *= 0.91
total_price = price * num_joinery

if receiving_way == "With delivery":
    total_price += 60
if num_joinery < 10:
    print(f"Invalid order")
elif num_joinery > 99:
    total_price *= 0.96
    print(f"{total_price:.2f} BGN")
else:
    print(f"{total_price:.2f} BGN")
