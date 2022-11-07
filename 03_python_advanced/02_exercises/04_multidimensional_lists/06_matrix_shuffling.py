def validation_data(f_command, f_rows, f_columns):
    indexes = [int(el) for el in f_command[1:] if el.isdigit()]
    if not f_command[0] == "swap":
        return False
    elif not len(indexes) == 4:
        return False
    elif indexes[0] >= f_rows or indexes[0] < 0 or indexes[2] >= f_rows or indexes[2] < 0:
        return False
    elif indexes[1] >= f_columns or indexes[1] < 0 or indexes[3] >= f_columns or indexes[3] < 0:
        return False
    return True


def swap_command(f_command, f_matrix):
    row_1 = int(f_command[1])
    col_1 = int(f_command[2])
    row_2 = int(f_command[3])
    col_2 = int(f_command[4])
    matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
    return f_matrix


rows, columns = [int(el) for el in input().split()]

matrix = []

for _ in range(rows):
    matrix.append(input().split())

command = input()

while not command == "END":
    command = command.split()
    if validation_data(command, rows, columns):
        matrix = swap_command(command, matrix)
        for row_index in range(rows):
            print(*matrix[row_index])
    else:
        print("Invalid input!")
    command = input()
