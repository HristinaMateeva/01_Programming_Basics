n = int(input())

is_found = False
for a in range(1, 9 + 1):
    for b in range(9, 1, -1):
        for c in range(1, 9):
            for d in range(8, 0, -1):
                sum_nums = (a + b + c + d)
                multiplication_nums = (a * b * c * d)
                if sum_nums == multiplication_nums and n % 10 == 5:
                    is_found = True
                    print(f"{a}{b}{c}{d}")
                    exit()
                elif multiplication_nums // sum_nums == 3 and n % 3 == 0:
                    is_found = True
                    print(f"{d}{c}{b}{a}")
                    exit()

if not is_found:
    print("Nothing found")
    