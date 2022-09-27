import re

pattern = r"^@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+$"

number = int(input())

for num in range(number):
    sequence = input()
    match = re.findall(pattern, sequence)
    barcode = ""
    product_group = ""
    if match:
        barcode = ''.join(match)
        for char in barcode:
            if char.isdigit():
                product_group += char
        if not product_group:
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")
