command = input()

total_meters = 5364
counter_days = 1
target = 8848
is_climbed = False

while command != "END":
    night_stand = command
    climbed_meters = int(input())
    total_meters += climbed_meters
    if night_stand == "Yes":
        counter_days += 1
    if total_meters >= target:
        is_climbed = True
        break
    if counter_days > 5:
        total_meters -= climbed_meters
        break

    command = input()

if is_climbed:
    print(f"Goal reached for {counter_days} days!")
else:
    print("Failed!")
    print(f"{total_meters}")
