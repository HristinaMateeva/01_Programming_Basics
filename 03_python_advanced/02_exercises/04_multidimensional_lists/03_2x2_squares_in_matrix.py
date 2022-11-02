rows, columns = [int(el) for el in input().split()]

matrix = []
result = 0

for _ in range(rows):
    symbols = input().split()
    matrix.append(symbols)

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        # sub_matrix = [matrix[row_index][col_index], matrix[row_index][col_index + 1],
        #               matrix[row_index + 1][col_index], matrix[row_index + 1][col_index + 1]]
        if matrix[row_index][col_index] == matrix[row_index][col_index + 1] == \
                matrix[row_index + 1][col_index] == matrix[row_index + 1][col_index + 1]:
            result += 1

print(result)
