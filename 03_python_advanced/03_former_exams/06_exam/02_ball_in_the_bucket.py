def is_inside(f_row, f_col, size):
    if 0 <= f_row < size and 0 <= f_col < size:
        return True
    return False


SIZE = 6
num_turns = 3

matrix = []
total_scores = 0
prize = ""

for row_matrix in range(SIZE):
    line = input().split()
    matrix.append(line)

for num in range(num_turns):
    row, col = [int(x) for x in input().strip("()").split(", ")]
    if not is_inside(row, col, SIZE):
        continue

    elif matrix[row][col].isdigit():
        continue

    elif matrix[row][col] == "*":
        pass

    elif matrix[row][col] == "B":
        matrix[row][col] = "*"
        for bucket_row in range(SIZE):
            score = matrix[bucket_row][col]
            if score.isdigit():
                total_scores += int(score)

if total_scores < 100:
    needed_scores = 100 - total_scores
    print(f"Sorry! You need {needed_scores} points more to win a prize.")
else:
    if 100 <= total_scores < 200:
        prize = "Football"
    elif 200 <= total_scores < 300:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"
    print(f"Good job! You scored {total_scores} points, and you've won {prize}.")
