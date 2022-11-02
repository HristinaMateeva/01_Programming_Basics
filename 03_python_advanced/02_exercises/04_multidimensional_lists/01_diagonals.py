size = int(input())

matrix = []
primary = []
secondary = []

for _ in range(size):
    matrix.append([int(x) for x in input().split(", ")])

for inx in range(size):
    primary.append(matrix[inx][inx])
    secondary.append(matrix[inx][size - 1 - inx])

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")
