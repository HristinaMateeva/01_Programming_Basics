strawberry_price = float(input())
bananas_quantity = float(input())
oranges_quantity = float(input())
raspberries_quantity = float(input())
strawberries_quantity = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price * 0.60
bananas_price = raspberries_price * 0.20

total_price = (strawberry_price * strawberries_quantity) + \
              (bananas_price * bananas_quantity) + \
              (raspberries_price * raspberries_quantity) + \
              (oranges_price * oranges_quantity)

print(f"{total_price:.2f}")
