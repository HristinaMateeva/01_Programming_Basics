x = float(input())
y = float(input())
h = float(input())
green_paint_liter = 3.4
red_paint_liter = 4.3
area_fwd_aft = (x * x - 1.2 * 2) + x * x
area_side = 2 * (x * y - 1.5 * 1.5)
area_roof_fwd_aft = x * h  #Може да се напише и така: 2 * x * h / 2 или 2 * ((x * h) / 2)
area_roof_side = 2 * (x * y)
total_paint_walls = (area_fwd_aft + area_side) / 3.4
total_paint_roof = (area_roof_fwd_aft + area_roof_side) / 4.3
print(f"{total_paint_walls:.2f}")
print(f"{total_paint_roof:.2f}")
