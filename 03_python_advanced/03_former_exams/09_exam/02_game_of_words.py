def is_inside(f_row, f_col, size):
    if 0 <= f_row < size and 0 <= f_col < size:
        return True
    return False


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


initial_string = input()
size = int(input())

matrix = []
player_row = ""
player_col = ""

for row_matrix in range(size):
    line = list(input())
    matrix.append(line)

    if "P" in matrix[row_matrix]:
        player_row = row_matrix
        player_col = line.index("P")

num_commands = int(input())

for num in range(num_commands):
    direction = input()
    current_row = player_row
    current_col = player_col

    if direction == "up":
        player_row, player_col = move_up(player_row, player_col)
    elif direction == "down":
        player_row, player_col = move_down(player_row, player_col)
    elif direction == "left":
        player_row, player_col = move_left(player_row, player_col)
    elif direction == "right":
        player_row, player_col = move_right(player_row, player_col)

    if is_inside(player_row, player_col, size):
        matrix[current_row][current_col] = "-"
        current_value = matrix[player_row][player_col]
        if current_value.isalpha() and not current_value == "P":
            initial_string += current_value
        matrix[player_row][player_col] = "P"

    elif not is_inside(player_row, player_col, size) and initial_string:
        player_row = current_row
        player_col = current_col
        initial_string = initial_string[:-1]
        continue


print(initial_string)

for m_row in range(len(matrix)):
    print(''.join(matrix[m_row]))
