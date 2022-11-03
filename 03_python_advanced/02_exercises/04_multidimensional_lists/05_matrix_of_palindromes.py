rows, columns = [int(el) for el in input().split()]

matrix = []
start_symbol_ord = ord("a")
middle_symbol_ord = ord("a")

for row in range(rows):
    matrix.append(list())
    middle_symbol_ord = ord("a") + row
    for column in range(columns):
        matrix[row].append(f"{chr(start_symbol_ord)}{chr(middle_symbol_ord)}{chr(start_symbol_ord)}")
        middle_symbol_ord += 1
    start_symbol_ord += 1
    print(*matrix[row])
