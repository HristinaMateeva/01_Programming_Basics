import math

height_wall = int(input())
width_wall = int(input())
percent_windows_doors = int(input())

total_area = math.ceil(height_wall * width_wall * 4)
total_painting_area_left = total_area * (100 - percent_windows_doors) / 100
paint_left = 0
is_painted = False

command = input()

while command != "Tired!":
    liters_paint = int(command)
    total_painting_area_left -= liters_paint

    if total_painting_area_left <= 0:
        paint_left = abs(total_painting_area_left)
        is_painted = True
        break

    command = input()

if command == "Tired!":
    print(f"{round(total_painting_area_left)} quadratic m left." )
elif is_painted and paint_left == 0:
    print("All walls are painted! Great job, Pesho!")
elif is_painted and paint_left > 0:
    print(f"All walls are painted and you have {round(paint_left)} l paint left!")
