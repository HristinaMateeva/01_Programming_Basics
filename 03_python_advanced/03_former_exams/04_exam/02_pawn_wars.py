SIZE = 8

matrix = []
MAPPER = []
map_letter = chr(97)
map_num = 9
white_position = ""
black_position = ""
current_turn = 1  # white pawn turn = 1, black pawn turn = 2
current_pawn = ""

pawns_directions = {
    "white_forward": (-1, 0),
    "black_forward": (1, 0),
    "white_up_left": (-1, -1),
    "white_up_right": (-1, 1),
    "black_down_left": (1, -1),
    "black_down_right": (1, 1)
}

# Creating the MAPPER
for map_row in range(SIZE):
    MAPPER.append([])
    map_num -= 1
    for map_col in range(SIZE):
        MAPPER[map_row].append(f"{map_letter}{map_num}")
        map_letter = chr(ord(map_letter) + 1)
    map_letter = chr(97)

# Creating the playing board and defining the positions of the pawns
for matrix_row in range(SIZE):
    line = input().split()
    matrix.append(line)

    if "w" in line:
        white_position = [matrix_row, line.index("w")]

    if "b" in line:
        black_position = [matrix_row, line.index("b")]

while True:

    # white pawn turn
    if current_turn == 1:
        current_pawn = "White"
        # Checking if the black pawn can be captured by the white one
        row = white_position[0]
        col = white_position[1]
        # Checking the left diagonal
        if not col == 0:
            left_diagonal = [pawns_directions["white_up_left"][0], pawns_directions["white_up_left"][1]]
            if matrix[row + left_diagonal[0]][col + left_diagonal[1]] == "b":
                mapper_white_position = MAPPER[row + left_diagonal[0]][col + left_diagonal[1]]
                print(f"Game over! {current_pawn} win, capture on {mapper_white_position}.")
                break
        if not col == 7:
            right_diagonal = [pawns_directions["white_up_right"][0], pawns_directions["white_up_right"][1]]
            # Checking the right diagonal
            if matrix[row + right_diagonal[0]][col + right_diagonal[1]] == "b":
                mapper_white_position = MAPPER[row + right_diagonal[0]][col + right_diagonal[1]]
                print(f"Game over! {current_pawn} win, capture on {mapper_white_position}.")
                break

        # Since the black pawn cannot be captured, then the white pawn is moving forward
        matrix[white_position[0]][white_position[1]] = "-"
        row = white_position[0] + pawns_directions["white_forward"][0]
        col = white_position[1] + pawns_directions["white_forward"][1]
        white_position = [row, col]
        matrix[row][col] = "w"

        # Checking if the white pawn is on the final row
        if white_position[0] == 0:
            print(f"Game over! {current_pawn} pawn is promoted to a queen at {MAPPER[row][col]}.")
            break

    # black pawn turn
    elif current_turn == 2:
        current_pawn = "Black"
        # Checking if the white pawn can be captured by the black one
        row = black_position[0]
        col = black_position[1]
        # Checking the left diagonal
        if not col == 0:
            left_diagonal = [pawns_directions["black_down_left"][0], pawns_directions["black_down_left"][1]]
            if not col == 0 and matrix[row + left_diagonal[0]][col + left_diagonal[1]] == "w":
                mapper_black_position = MAPPER[row + left_diagonal[0]][col + left_diagonal[1]]
                print(f"Game over! {current_pawn} win, capture on {mapper_black_position}.")
                break
        # Checking the right diagonal
        if not col == 7:
            right_diagonal = [pawns_directions["black_down_right"][0], pawns_directions["black_down_right"][1]]
            if matrix[row + right_diagonal[0]][col + right_diagonal[1]] == "w":
                mapper_black_position = MAPPER[row + right_diagonal[0]][col + right_diagonal[1]]
                print(f"Game over! {current_pawn} win, capture on {mapper_black_position}.")
                break

        # Since the white pawn cannot be captured, then the black pawn is moving forward
        matrix[black_position[0]][black_position[1]] = "-"
        row = black_position[0] + pawns_directions["black_forward"][0]
        col = black_position[1] + pawns_directions["black_forward"][1]
        black_position = [row, col]
        matrix[row][col] = "b"

        # Checking if the black pawn is on the final row
        if black_position[0] == 7:
            print(f"Game over! {current_pawn} pawn is promoted to a queen at {MAPPER[row][col]}.")
            break

    # Changing the turn
    current_turn += 1
    if current_turn == 3:
        current_turn = 1
