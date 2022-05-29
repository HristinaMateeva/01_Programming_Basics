target = int(input())

total_price = 0
command = input()
is_target_reached = False

while command != "closed":
    type_procedure = command
    if type_procedure == "haircut":
        gender = input()
        if gender == "mens":
            total_price += 15
        elif gender == "ladies":
            total_price += 20
        elif gender == "kids":
            total_price += 10
    elif type_procedure == "color":
        coloring_type = input()
        if coloring_type == "touch up":
            total_price += 20
        elif coloring_type == "full color":
            total_price += 30
    if total_price >= target:
        is_target_reached = True
        break
    command = input()

difference = abs(total_price - target)

if is_target_reached:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {difference}lv. more.")
print(f"Earned money: {total_price}lv.")
