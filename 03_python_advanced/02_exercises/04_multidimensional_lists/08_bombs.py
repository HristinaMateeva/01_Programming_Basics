def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    # row - 1, col
    size = len(matrix)
    neighbours = []
    if is_inside(row - 1, col, size) and matrix[row - 1][col] > 0:
        neighbours.append([row - 1, col])
    # row + 1, col
    if is_inside(row + 1, col, size) and matrix[row + 1][col] > 0:
        neighbours.append([row + 1, col])
    # row, col - 1
    if is_inside(row, col - 1, size) and matrix[row][col - 1] > 0:
        neighbours.append([row, col - 1])
    # row, col + 1
    if is_inside(row, col + 1, size) and matrix[row][col + 1] > 0:
        neighbours.append([row, col + 1])
    # row - 1, col - 1
    if is_inside(row - 1, col - 1, size) and matrix[row - 1][col - 1] > 0:
        neighbours.append([row - 1, col - 1])
    # row - 1, col + 1
    if is_inside(row - 1, col + 1, size) and matrix[row - 1][col + 1] > 0:
        neighbours.append([row - 1, col + 1])
    # row + 1, col - 1
    if is_inside(row + 1, col - 1, size) and matrix[row + 1][col - 1] > 0:
        neighbours.append([row + 1, col - 1])
    # row + 1, col + 1
    if is_inside(row + 1, col + 1, size) and matrix[row + 1][col + 1] > 0:
        neighbours.append([row + 1, col + 1])
    return neighbours


n = int(input())

matrix = []

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

bombs = input().split()

for bomb_coordinates in bombs:
    bomb_row, bomb_col = [int(x) for x in bomb_coordinates.split(",")]
    if matrix[bomb_row][bomb_col] <= 0:
        continue

    bomb_power = matrix[bomb_row][bomb_col]
    matrix[bomb_row][bomb_col] = 0
    neighbours = get_neighbours(bomb_row, bomb_col, matrix)

    for row, col in neighbours:
        matrix[row][col] -= bomb_power

alive_cells = 0
alive_sells_sum = 0

for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            alive_sells_sum += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {alive_sells_sum}")

for row in matrix:
    print(*row, sep=" ")
