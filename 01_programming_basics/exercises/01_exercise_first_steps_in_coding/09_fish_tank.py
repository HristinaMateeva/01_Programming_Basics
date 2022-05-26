length_cm = int(input())
width_cm = int(input())
height_cm = int(input())
capacity_percent = float(input())
empty_volume_tank_cm = length_cm * width_cm * height_cm
# 1 liter is equal to 1 dm^3
empty_volume_tank_liters = empty_volume_tank_cm * 0.001  # volume_tank_cm / 1000
capacity_water = capacity_percent / 100
needed_water = empty_volume_tank_liters * (1 - capacity_water)
print(needed_water)
