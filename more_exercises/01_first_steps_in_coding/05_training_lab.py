width_meter = float(input())
height_meter = float(input())
width_cm = width_meter * 100
height_cm = height_meter * 100
row_seats = (height_cm - 100) // 70
column_seats = width_cm // 120
total_seats = row_seats * column_seats - 3

print(total_seats)
