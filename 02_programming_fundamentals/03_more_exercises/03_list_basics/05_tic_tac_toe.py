first_line = [int(el) for el in input().split()]
second_line = [int(el) for el in input().split()]
third_line = [int(el) for el in input().split()]

winner = ""
first_column = [first_line[0], second_line[0], third_line[0]]
second_column = [first_line[1], second_line[1], third_line[1]]
third_column = [first_line[2], second_line[2], third_line[2]]

for index in range(len(first_line)):
    if first_line[index] == second_line[index] == third_line[index]:
        if first_line[index] == 1:
            winner = "First"
        elif first_line[index] == 2:
            winner = "Second"

for index in range(len(first_column)):
    if first_column[index] == second_column[index] == third_column[index]:
        if first_column[index] == 1:
            winner = "First"
        elif first_column[index] == 2:
            winner = "Second"

if first_line[0] == second_line[1] == third_line[2]:
    if first_line[0] == 1:
        winner = "First"
    elif first_line[0] == 2:
        winner = "Second"

if first_line[2] == second_line[1] == third_line[0]:
    if first_line[2] == 1:
        winner = "First"
    elif first_line[2] == 2:
        winner = "Second"

if not winner:
    print("Draw!")
else:
    print(f"{winner} player won")
