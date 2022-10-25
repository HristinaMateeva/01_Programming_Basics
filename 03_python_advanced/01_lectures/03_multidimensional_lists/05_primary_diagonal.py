n = int(input())

matrix = []
diagonal = 0

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for row_index in range(n):
    for col_index in range(n):
        if row_index == col_index:
            diagonal += matrix[row_index][col_index]

print(diagonal)
