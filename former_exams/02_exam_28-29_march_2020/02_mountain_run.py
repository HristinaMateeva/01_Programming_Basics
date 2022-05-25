import math

record_seconds = float(input())
distance_meters = float(input())
time_seconds_per_meter = float(input())

needed_seconds = distance_meters * time_seconds_per_meter
delay = math.floor(distance_meters // 50)
delay_total = delay * 30
total_seconds = needed_seconds + delay_total

difference = abs(total_seconds - record_seconds)
if record_seconds > total_seconds:
    print(f"Yes! The new record is {total_seconds:.2f} seconds.")
else:
    print(f"No! He was {difference:.2f} seconds slower.")
