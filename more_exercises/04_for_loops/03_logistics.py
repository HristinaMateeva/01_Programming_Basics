num_cargo = int(input())

total_price_microbus = 0
tons_microbus = 0
total_price_truck = 0
tons_truck = 0
total_price_train = 0
tons_train = 0

for num in range(1, num_cargo + 1):
    cargo_tons = int(input())
    if cargo_tons <= 3:
        tons_microbus += cargo_tons
        total_price_microbus = tons_microbus * 200
    elif cargo_tons <= 11:
        tons_truck += cargo_tons
        total_price_truck = tons_truck * 175
    elif cargo_tons >= 12:
        tons_train += cargo_tons
        total_price_train = tons_train * 120

total_tons = tons_microbus + tons_truck + tons_train
average_cargo = (total_price_microbus + total_price_truck + total_price_train) / total_tons
percent_microbus = tons_microbus / total_tons * 100
percent_truck = tons_truck / total_tons * 100
percent_train = tons_train / total_tons * 100

print(f"{average_cargo:.2f}")
print(f"{percent_microbus:.2f}%")
print(f"{percent_truck:.2f}%")
print(f"{percent_train:.2f}%")
