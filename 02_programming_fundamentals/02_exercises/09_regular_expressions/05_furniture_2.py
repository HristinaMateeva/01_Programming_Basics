import re

command = input()
pattern = r"^>>(?P<furniture>[a-zA-Z]+)<<(?P<price>\d+(\.\d)?)!(?P<quantity>\d+)$"
current_price = 0
total_price = 0
furniture_list = []

while not command == "Purchase":
    matches = re.match(pattern, command)
    if matches:
        furniture = matches.group('furniture')
        price = float(matches.group('price'))
        quantity = int(matches.group('quantity'))
        current_price = price * quantity
        furniture_list.append(furniture)
        total_price += current_price

    command = input()

print("Bought furniture:")
for item in furniture_list:
    print(f"{item}")
print(f"Total money spend: {total_price:.2f}")
