command = input()

products = {}

while not command == "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in products:
        products[product] = {"price": price, "quantity": quantity}
    else:
        products[product]["price"] = price
        products[product]["quantity"] += quantity

    command = input()

for key, value in products.items():
    total_price = value["price"] * value["quantity"]
    print(f"{key} -> {total_price:.2f}")
