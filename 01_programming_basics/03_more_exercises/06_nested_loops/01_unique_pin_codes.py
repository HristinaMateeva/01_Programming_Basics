max_first_num = int(input())
max_second_num = int(input())
max_third_num = int(input())

first_num = 0
second_num = 0
third_num = 0
valid_first_num = False
valid_second_num = False
valid_third_num = False

for f in range(1, max_first_num + 1):
    for s in range(1, max_second_num + 1):
        for t in range(1, max_third_num + 1):
            if f % 2 == 0:
                first_num = f
                valid_first_num = True
                if s == 2 or s == 3 or s == 5 or s == 7:
                    second_num = s
                    valid_second_num = True
                    if t % 2 == 0:
                        third_num = t
                        valid_third_num = True
                        if valid_first_num and valid_second_num and valid_third_num:
                            print(f"{first_num} {second_num} {third_num}")
