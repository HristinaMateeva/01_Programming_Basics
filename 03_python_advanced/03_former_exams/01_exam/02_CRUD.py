matrix = []

for i in range(6):
    line = input().split()
    matrix.append(line)

position = input()
row = int(position[1])
col = int(position[-2])

command = input()

while not command == "Stop":
    command_elements = command.split(", ")
    action = command_elements[0]
    direction = command_elements[1]

    if direction == "up":
        row -= 1
    elif direction == "down":
        row += 1
    elif direction == "left":
        col -= 1
    elif direction == "right":
        col += 1

    current_position = matrix[row][col]
    if action == "Create":
        value = command_elements[2]
        if current_position == ".":
            matrix[row][col] = value

    elif action == "Update":
        value = command_elements[2]
        if current_position != ".":
            matrix[row][col] = value

    elif action == "Delete":
        if current_position != ".":
            matrix[row][col] = "."

    elif action == "Read":
        if current_position != ".":
            print(matrix[row][col])

    command = input()

for m_line in matrix:
    print(" ".join(m_line))
