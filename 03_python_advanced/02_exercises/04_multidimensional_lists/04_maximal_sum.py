from sys import maxsize

rows, columns = [int(el) for el in input().split()]

matrix = []
max_sum = -maxsize
max_sub_matrix = []
best_row = 0
best_col = 0

for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for row_idx in range(rows - 2):
    for col_idx in range(columns - 2):
        sub_matrix = [matrix[row_idx][col_idx], matrix[row_idx][col_idx + 1], matrix[row_idx][col_idx + 2],
                      matrix[row_idx + 1][col_idx], matrix[row_idx + 1][col_idx + 1], matrix[row_idx + 1][col_idx + 2],
                      matrix[row_idx + 2][col_idx], matrix[row_idx + 2][col_idx + 1], matrix[row_idx + 2][col_idx + 2]]
        current_sum = sum(sub_matrix)
        if current_sum > max_sum:
            max_sum = current_sum
            max_sub_matrix = sub_matrix.copy()

print(f"Sum = {max_sum}")
print(max_sub_matrix[0], max_sub_matrix[1], max_sub_matrix[2])
print(max_sub_matrix[3], max_sub_matrix[4], max_sub_matrix[5])
print(max_sub_matrix[6], max_sub_matrix[7], max_sub_matrix[8])
