import math

budget = float(input())
student = int(input())
package_of_floor = float(input())
price_for_one_egg = float(input())
price_for_one_apron = float(input())

floor_packages = 0

price_for_apron = price_for_one_apron * math.ceil(student * 1.2)
# price_for_apron = math.ceil(price_for_one_apron * student) * 1.2

for numbers in range(1, student + 1):
    if numbers % 5 == 0:
        continue
    else:
        floor_packages += 1

price_for_all = price_for_apron + (price_for_one_egg * 10) * student + floor_packages * package_of_floor

needed_money = abs(budget - price_for_all)

if budget >= price_for_all:
    print(f"Items purchased for {price_for_all:.2f}$.")
else:
    print(f"{needed_money:.2f}$ more needed.")
