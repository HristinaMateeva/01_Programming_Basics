days_of_plunder = int(input())
daily_plunder = int(input())
expected_plunder = int(input())

total_gathered_plunder = 0

for day in range(1, days_of_plunder + 1):
    total_gathered_plunder += daily_plunder
    if day % 3 == 0:
        total_gathered_plunder += daily_plunder / 2
    if day % 5 == 0:
        total_gathered_plunder *= 0.7

if total_gathered_plunder >= expected_plunder:
    print(f"Ahoy! {total_gathered_plunder:.2f} plunder gained.")
else:
    percent = total_gathered_plunder / expected_plunder * 100
    print(f"Collected only {percent:.2f}% of the plunder.")
