command = input()

total_price_without_taxes = 0
is_price_valid = True
is_order_valid = True

while command != "special" or command != "regular":
    if command == "special" or command == "regular":  #added due to bug in PyCharm version
        break
    command = float(command)
    if command <= 0:
        is_price_valid = False
        print("Invalid price!")
    else:
        total_price_without_taxes += command

    command = input()

taxes = total_price_without_taxes * 0.2
total_price_with_taxes = total_price_without_taxes + taxes

if command == "special":
    total_price_with_taxes *= 0.9

if total_price_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total_price_without_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {total_price_with_taxes:.2f}$")
