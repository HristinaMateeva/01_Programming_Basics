# Index validation
def is_inside(f_row, f_col, size):
    if 0 <= f_row < size and 0 <= f_col < size:
        return True
    return False


# ------------------------------
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
    "down_left": (1, -1),
    "down_right": (1, 1)
}
# ------------------------------


def move_up(row, col):
    return row - 1, col


def move_down(row, col):
    return row + 1, col


def move_left(row, col):
    return row, col - 1


def move_right(row, col):
    return row, col + 1


def move_up_left(row, col):
    return row - 1, col -1


def move_up_right(row, col):
    return row - 1, col + 1


def move_down_left(row, col):
    return row + 1, col - 1


def move_down_right(row, col):
    return row + 1, col + 1

# If the player can continue on the next side
# def move_up(row, col, row_size):
#     if row == 0:
#         row = row_size
#     return row - 1, col
#
#
# def move_down(row, col, row_size):
#     if row == row_size - 1:
#         row = -1
#     return row + 1, col
#
#
# def move_left(row, col, col_size):
#     if col == 0:
#         col = col_size
#     return row, col - 1
#
#
# def move_right(row, col, col_size):
#     if col == col_size - 1:
#         col = -1
#     return row, col + 1
