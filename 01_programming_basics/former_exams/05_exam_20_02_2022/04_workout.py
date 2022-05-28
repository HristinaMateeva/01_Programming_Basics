import math

number_days = int(input())
km_first_day = float(input())

total_km = km_first_day
km_per_day = 0
target = 1000
total = 0

for num in range(1, number_days + 1):
    percent_increase = int(input())
    km_per_day = total_km * (percent_increase / 100)
    total_km += km_per_day
    total += total_km

sum_total = km_first_day + total
difference = math.ceil(abs(target - sum_total))

if sum_total >= target:
    print(f"You've done a great job running {difference} more kilometers!")
else:
    print(f"Sorry Mrs. Ivanova, you need to run {difference} more kilometers")
