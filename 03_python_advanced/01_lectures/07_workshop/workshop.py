class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


# Print matrix
def print_matrix(ma):
    for el in ma:
        print(el)


def validate_column_choice(selected_column_num, max_column_index):
    # Verify if the player choice of number of the column is correct
    if not (0 <= selected_column_num <= max_column_index):
        raise InvalidColumnError


def place_player_choice(ma, selected_column_index, f_player_num):
    # Place player marker on the spot.
    # Check if the column is full. If so, throw error.
    f_rows_count = len(ma)
    for row_index in range(f_rows_count - 1, -1, -1):
        current_element = ma[row_index][selected_column_index]
        if current_element == 0:
            ma[row_index][selected_column_index] = f_player_num
            return row_index, selected_column_index

    raise FullColumnError


def is_player_num(ma, f_row, f_col, f_player_num):
    if f_col < 0 or f_row < 0:
        return False
    try:
        if ma[f_row][f_col] == f_player_num:
            return True
    except IndexError:
        return False
    return False


def is_horizontal(ma, f_row, f_col, f_player_num, slots_count):
    """
    We check for both sides, because we have input like this:
    1
    1
    2
    2
    4
    4
    3
    If we do not check for both there will be a winner, but we can not now that
    Also we have to check for this condition:
    1, 1, 2, 2, 5, 5, 6, 6, 7, 7, 3
    [True, True, True, False, True, True, True] = This is not a winner
    """
    right = []
    for index in range(slots_count):
        if is_player_num(ma, f_row, f_col + index, f_player_num):
            right.append(True)
        else:
            break
    left = []
    for index in range(slots_count):
        if is_player_num(ma, f_row, f_col - index, f_player_num):
            left.append(True)
        else:
            break
    # count_right = [is_player_num(ma, row, col + index, player_num) for index in range(slots_count)].count(True)
    # count_left = [is_player_num(ma, row, col - index, player_num) for index in range(slots_count)].count(True)
    # TODO handle exception case
    # It should be strict ">" because we are counting the current as well
    return len(left + right) > slots_count


def is_right_diagonal(ma, f_row, f_col, f_player_num, slots_count):
    """
    We check for both (up right and left down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    right_up_count = [is_player_num(ma, f_row - index, f_col + index, f_player_num) for index in
                      range(slots_count)].count(True)
    left_down_count = [is_player_num(ma, f_row + index, f_col + index, f_player_num) for index in
                       range(slots_count)].count(True)
    return (right_up_count + left_down_count) > 4


def is_left_diagonal(ma, f_row, f_col, f_player_num, slots_count):
    """
    We check for both (up left and right down) so we can look for the same problem -
    adding element which is not only to one side with 4 but for both
    """
    left_up_count = [is_player_num(ma, f_row - index, f_col - index, f_player_num) for index in
                     range(slots_count)].count(True)
    left_down_count = [is_player_num(ma, f_row + index, f_col + index, f_player_num) for index in
                       range(slots_count)].count(True)
    return (left_up_count + left_down_count) > 4


def is_winner(ma, f_row, f_col, f_player_num, slots_count=4):
    """
    We check for horizontal(both sides)
    Only down (because we fill the matrix from bottom to top).
    Check for right and left diagonal
    """
    is_down = all([is_player_num(ma, f_row + index, f_col, f_player_num) for index in range(slots_count)])

    if any(
            [
                is_horizontal(ma, f_row, f_col, f_player_num, slots_count),
                is_right_diagonal(ma, f_row, f_col, f_player_num, slots_count),
                is_left_diagonal(ma, f_row, f_col, f_player_num, slots_count),
                is_down
            ]
    ):
        return True
    return False


rows_count = 6
cols_count = 7
counter_moves = 0
max_moves = rows_count * cols_count

# Create matrix
matrix = [[0 for _ in range(cols_count)] for row_num in range(rows_count)]
# Print initial board
print_matrix(matrix)

player_num = 1
while True:
    # Decide correct player num (only 1 and 2 are possible - only two players)
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # Read column choice from input
        column_num = int(input(f"Player {player_num}, please choose a column: ")) - 1
        validate_column_choice(column_num, cols_count - 1)
        row, col = place_player_choice(matrix, column_num, player_num)
        if is_winner(matrix, row, col, player_num):
            print_matrix(matrix)
            print(f"The winner is player {player_num}")
            break
        print_matrix(matrix)
    except InvalidColumnError:
        # Not in range of the game 1-7
        print(f"This colum is not valid> Please select a number between 1 and {cols_count}")
        continue
    except ValueError:
        # Not a valid number
        print("Please select a valid digit!")
        continue
    except FullColumnError:
        # This is already a full column
        print(f"This column is already full! Please select other column number")
        continue

    # Only if the turn was successful, we go to the next player
    player_num += 1
    counter_moves += 1
    # Checking if the board is full
    if counter_moves == max_moves:
        print("No more moves left! Game over!")
        break

# TODO: to correct the functions with the diagonals respectively like horizontal functions
