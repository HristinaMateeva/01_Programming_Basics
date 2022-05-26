command = input()

max_goals = 0
best_player = " "
is_max_goals_more_ten = False

while command != "END":
    name_player = command
    number_goals = int(input())

    if number_goals > max_goals:
        max_goals = number_goals
        best_player = name_player
    if number_goals >= 10:
        is_max_goals_more_ten = True
        break

    command = input()

print(f"{best_player} is the best player!")
if max_goals >= 3:
    print(f"He has scored {max_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {max_goals} goals.")
