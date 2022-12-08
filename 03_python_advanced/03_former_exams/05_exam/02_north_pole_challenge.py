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


def check_for_item(row, col, f_matrix, f_all_items, f_items):
    if f_matrix[row][col] == "D":
        f_all_items["D"] -= 1
        f_items["D"] += 1

    elif f_matrix[row][col] == "G":
        f_all_items["G"] -= 1
        f_items["G"] += 1

    elif f_matrix[row][col] == "C":
        f_all_items["C"] -= 1
        f_items["C"] += 1
    f_matrix[row][col] = "Y"
    return f_matrix, f_all_items, f_items


def if_all_items_collected(f_all_items):
    if f_all_items["D"] == 0 and f_all_items["G"] == 0 and f_all_items["C"] == 0:
        return True
    return False


size_row, size_col = [int(el) for el in input().split(", ")]

matrix = []
player_row = ""
player_col = ""

all_items_collected = False
items = {"D": 0, "G": 0, "C": 0}
all_items = {"D": 0, "G": 0, "C": 0}

for m_row in range(size_row):
    line = input().split()
    matrix.append(line)

    if "Y" in matrix[m_row]:
        player_row = m_row
        player_col = line.index("Y")

    if "D" in matrix[m_row]:
        all_items["D"] += matrix[m_row].count("D")

    if "G" in matrix[m_row]:
        all_items["G"] += matrix[m_row].count("G")

    if "C" in matrix[m_row]:
        all_items["C"] += matrix[m_row].count("C")


command = input()

while not command == "End":
    direction, steps = command.split("-")
    steps = int(steps)
    if direction == "up":
        while steps > 0:
            matrix[player_row][player_col] = "x"
            player_row, player_col = move_up(player_row, player_col, size_row)
            matrix, all_items, items = check_for_item(player_row, player_col, matrix, all_items, items)
            if if_all_items_collected(all_items):
                all_items_collected = True
                break
            steps -= 1

    elif direction == "down":
        while steps > 0:
            matrix[player_row][player_col] = "x"
            player_row, player_col = move_down(player_row, player_col, size_row)
            matrix, all_items, items = check_for_item(player_row, player_col, matrix, all_items, items)
            if if_all_items_collected(all_items):
                all_items_collected = True
                break
            steps -= 1

    elif direction == "left":
        while steps > 0:
            matrix[player_row][player_col] = "x"
            player_row, player_col = move_left(player_row, player_col, size_col)
            matrix, all_items, items = check_for_item(player_row, player_col, matrix, all_items, items)
            if if_all_items_collected(all_items):
                all_items_collected = True
                break
            steps -= 1

    elif direction == "right":
        while steps > 0:
            matrix[player_row][player_col] = "x"
            player_row, player_col = move_right(player_row, player_col, size_col)
            matrix, all_items, items = check_for_item(player_row, player_col, matrix, all_items, items)
            if if_all_items_collected(all_items):
                all_items_collected = True
                break
            steps -= 1
    if all_items_collected:
        break

    command = input()

if all_items_collected:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {items['D']} Christmas decorations")
print(f"- {items['G']} Gifts")
print(f"- {items['C']} Cookies")

for matrix_row in matrix:
    print(' '.join(matrix_row))
