n = int(input())

matrix = []
diagonal = 0

for _ in range(n):
    nums = [int(el) for el in input().split()]
    matrix.append(nums)

for index in range(n):
    diagonal += matrix[index][index]

print(diagonal)
