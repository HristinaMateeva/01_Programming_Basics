data = input()

qty_dict = {}
price_dict = {}
result_dict = {}

while not data == "buy":
    product_name, product_price, product_quantity = data.split()
    product_price = float(product_price)
    product_quantity = int(product_quantity)
    if product_name in qty_dict:
        qty_dict[product_name] += product_quantity
    else:
        qty_dict[product_name] = product_quantity
    price_dict[product_name] = product_price

    data = input()

for key, value in qty_dict.items():
    result_dict[key] = qty_dict.get(key) * price_dict.get(key)

for product, total_price in result_dict.items():
    print(f"{product} -> {total_price:.2f}")
