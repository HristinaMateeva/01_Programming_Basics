def is_inside(f_row, f_col, size):
    if 0 <= f_row < size and 0 <= f_col < size:
        return True
    return False


def player_turn(f_row, f_col, f_matrix, player, scores, throws, size, f_result):
    throws += 1
    if is_inside(f_row, f_col, size):
        target = f_matrix[f_row][f_col]

        if target.isdigit():
            scores -= int(target)
        elif target == "B":
            f_result["winner"] = player
            f_result["winner_throws"] = throws
        else:
            # Finding the four corresponding numbers and adding their value to the sum of the numbers
            sum_corresponding_numbers = 0
            for row_or_col in range(size):
                if f_matrix[row_or_col][f_col].isdigit():
                    sum_corresponding_numbers += int(f_matrix[row_or_col][f_col])
                if matrix[f_row][row_or_col].isdigit():
                    sum_corresponding_numbers += int(matrix[f_row][row_or_col])

            if target == "D":
                scores -= (sum_corresponding_numbers * 2)
            elif target == "T":
                scores -= (sum_corresponding_numbers * 3)

        if scores <= 0:
            f_result["winner"] = player
            f_result["winner_throws"] = throws
    return f_matrix, scores, throws, f_result


SIZE = 7

first_player, second_player = input().split(", ")

matrix = []
first_player_scores = 501
second_player_scores = 501
first_player_throws = 0
second_player_throws = 0
result = {"winner": "", "winner_throws": 0}

for row_matrix in range(SIZE):
    line = input().split()
    matrix.append(line)

command = input()
current_player = first_player

while command:
    row, col = [int(x) for x in command.strip("()").split(", ")]

    if current_player == first_player:
        matrix, first_player_scores, first_player_throws, result = \
            player_turn(row, col, matrix, first_player, first_player_scores, first_player_throws, SIZE, result)

        if first_player in result.values():
            break

    else:
        matrix, second_player_scores, second_player_throws, result = \
            player_turn(row, col, matrix, second_player, second_player_scores, second_player_throws, SIZE, result)

        if second_player in result.values():
            break

    # Changing the turn of the players
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player

    command = input()

print(f"{result['winner']} won the game with {result['winner_throws']} throws!")
