number = int(input())

is_lucky = False

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                sum_left = a + b
                sum_right = c + d
                if sum_left == sum_right and number % sum_left == 0:
                    is_lucky = True
                    print(f"{a}{b}{c}{d}", end=" ")
                else:
                    is_lucky = False
                    continue
