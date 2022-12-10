def move_up(row, col, row_size):
    if row == 0:
        row = row_size
    return row - 1, col


def move_down(row, col, row_size):
    if row == row_size - 1:
        row = -1
    return row + 1, col


def move_left(row, col, col_size):
    if col == 0:
        col = col_size
    return row, col - 1


def move_right(row, col, col_size):
    if col == col_size - 1:
        col = -1
    return row, col + 1


size = int(input())

matrix = []
player_row = ""
player_col = ""
total_coins = 0
winner = False

for row_matrix in range(size):
    line = input().split()
    matrix.append(line)

    if "P" in matrix[row_matrix]:
        player_row = row_matrix
        player_col = line.index("P")

direction = input()
path = [[player_row, player_col]]

while direction:
    matrix[player_row][player_col] = "*"
    if direction == "up":
        player_row, player_col = move_up(player_row, player_col, size)
    elif direction == "down":
        player_row, player_col = move_down(player_row, player_col, size)
    elif direction == "left":
        player_row, player_col = move_left(player_row, player_col, size)
    elif direction == "right":
        player_row, player_col = move_right(player_row, player_col, size)
    else:
        direction = input()
        continue

    path.append([player_row, player_col])

    if matrix[player_row][player_col] == "X":
        total_coins /= 2
        break
    elif matrix[player_row][player_col].isdigit():
        total_coins += int(matrix[player_row][player_col])

    matrix[player_row][player_col] = "P"
    if total_coins >= 100:
        winner = True
        break
    direction = input()

if winner:
    print(f"You won! You've collected {total_coins} coins.")
else:
    print(f"Game over! You've collected {int(total_coins)} coins.")

print("Your path:")
for el in path:
    print(el)
