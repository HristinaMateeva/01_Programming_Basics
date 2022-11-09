def position_check(f_position):
    if f_position == len(snake) - 1:
        f_position = 0
    else:
        f_position += 1
    return f_position


rows, columns = [int(el) for el in input().split()]
snake = list(input())

matrix = []
position = 0

for row_index in range(rows):
    matrix.append(list())
    if row_index % 2 == 0:
        for col_index_1 in range(columns):
            matrix[row_index].append(snake[position])
            position = position_check(position)
    else:
        for col_index_2 in range(columns - 1, -1, -1):
            matrix[row_index].insert(0, snake[position])
            position = position_check(position)

for row in range(rows):
    print(''.join(matrix[row]))
