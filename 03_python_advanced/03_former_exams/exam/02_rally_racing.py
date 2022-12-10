def is_inside(f_row, f_col, f_size):
    if 0 <= f_row < f_size and 0 <= f_col < f_size:
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


size = int(input())
racing_num = input()

matrix = []
racer_row = 0
racer_col = 0
passed_distance = 0
is_disqualified = True
is_winner = False
tunnel_coordinates = []

for matrix_row in range(size):
    line = input().split()
    matrix.append(line)

    if "T" in matrix[matrix_row]:
        coords = [matrix_row, line.index("T")]
        tunnel_coordinates.append(coords)

if matrix[racer_row][racer_col] == "F":
    passed_distance += 10
    is_disqualified = False
    is_winner = True

matrix[racer_row][racer_col] = "C"

direction = input()

while not direction == "End":
    current_row = racer_row
    current_col = racer_col
    if direction == "up":
        racer_row, racer_col = move_up(racer_row, racer_col)
    elif direction == "down":
        racer_row, racer_col = move_down(racer_row, racer_col)
    elif direction == "left":
        racer_row, racer_col = move_left(racer_row, racer_col)
    elif direction == "right":
        racer_row, racer_col = move_right(racer_row, racer_col)

    if not is_inside(racer_row, racer_col, size):
        racer_row = current_row
        racer_col = current_col
        direction = input()
        continue

    if matrix[racer_row][racer_col] == "F":
        matrix[current_row][current_col] = "."
        matrix[racer_row][racer_col] = "C"
        passed_distance += 10
        is_winner = True
        is_disqualified = False
        break

    elif matrix[racer_row][racer_col] == "T":
        passed_distance += 30
        current_coordinates_tunnel = [racer_row, racer_col]
        matrix[racer_row][racer_col] = "."

        if current_coordinates_tunnel == tunnel_coordinates[0]:
            racer_row = tunnel_coordinates[1][0]
            racer_col = tunnel_coordinates[1][1]

        elif current_coordinates_tunnel == tunnel_coordinates[1]:
            racer_row = tunnel_coordinates[0][0]
            racer_col = tunnel_coordinates[0][1]

    else:
        passed_distance += 10
    matrix[current_row][current_col] = "."
    matrix[racer_row][racer_col] = "C"

    direction = input()

if is_disqualified:
    print(f"Racing car {racing_num} DNF.")

if is_winner:
    print(f"Racing car {racing_num} finished the stage!")

print(f"Distance covered {passed_distance} km.")
for m_row in matrix:
    print(''.join(m_row))
