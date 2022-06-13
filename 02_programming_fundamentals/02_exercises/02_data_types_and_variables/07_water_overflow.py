num_lines = int(input())

capacity = 255
water_counter = 0

for num in range(1, num_lines + 1):
    liters_of_water = int(input())
    if capacity - liters_of_water < 0:
        print("Insufficient capacity!")
        continue
    water_counter += liters_of_water
    capacity -= liters_of_water

print(f"{water_counter}")
