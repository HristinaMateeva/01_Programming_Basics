import re

pattern_customer = r"%(?P<customer>[A-Z][a-z]+)%"
pattern_product = r"\<(?P<product>.+)>"
pattern_count = r"\|(?P<count>[0-9]*)\|"
pattern_price = r"(?P<price>[0-9]+([.0-9])*)\$"

command = input()
final_data = {}
total_money = 0

while not command == "end of shift":
    current_customer = {}
    current_product = {}
    current_count = {}
    current_price = {}
    match_customer = re.finditer(pattern_customer, command)
    match_product = re.finditer(pattern_product, command)
    match_count = re.finditer(pattern_count, command)
    match_price = re.finditer(pattern_price, command)
    for customer in match_customer:
        current_customer = customer.groupdict()
    for product in match_product:
        current_product = product.groupdict()
    for count in match_count:
        current_count = count.groupdict()
    for price in match_price:
        current_price = price.groupdict()
    if current_customer and current_product and current_count and current_price:
        current_qty = int(current_count['count'])
        price_per_product = float(current_price['price'])
        current_total_price = current_qty * price_per_product
        final_data = {'customer': current_customer['customer'], 'product': current_product['product'], 'price': current_total_price}
        total_money += current_total_price
        print(f"{final_data['customer']}: {final_data['product']} - {current_total_price:.2f}")
    command = input()

print(f"Total income: {total_money:.2f}")

#90 % in Judge