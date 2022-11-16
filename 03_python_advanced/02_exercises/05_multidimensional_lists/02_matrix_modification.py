def index_validation(f_command, num):
    row_index = int(f_command[1])
    col_index = int(f_command[2])
    if 0 <= row_index < num and 0 <= col_index < num:
        return True
    return False


def add_command(f_command, f_matrix):
    row_index = int(f_command[1])
    col_index = int(f_command[2])
    value = int(f_command[3])
    f_matrix[row_index][col_index] += value
    return f_matrix


def subtract_command(f_command, f_matrix):
    row_index = int(f_command[1])
    col_index = int(f_command[2])
    value = int(f_command[3])
    f_matrix[row_index][col_index] -= value
    return f_matrix


number = int(input())

matrix = []

for _ in range(number):
    values = [int(el) for el in input().split()]
    matrix.append(values)

command = input()

while not command == "END":
    command = command.split()
    if index_validation(command, number):
        if command[0] == "Add":
            matrix = add_command(command, matrix)
        elif command[0] == "Subtract":
            matrix = subtract_command(command, matrix)
    else:
        print("Invalid coordinates")
    command = input()

for row in range(len(matrix)):
    print(*matrix[row])
