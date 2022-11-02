size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split()])

for inx in range(size):
    primary.append(matrix[inx][inx])
    secondary.append(matrix[inx][size - 1 - inx])

result = abs(sum(primary) - sum(secondary))

print(result)
