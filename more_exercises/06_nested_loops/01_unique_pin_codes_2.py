max_first_num = int(input())
max_second_num = int(input())
max_third_num = int(input())

first_num = 0
second_num = 0
third_num = 0

for f in range(1, max_first_num + 1):
    for s in range(1, max_second_num + 1):
        for t in range(1, max_third_num + 1):
            if f % 2 == 0 and (s == 2 or s == 3 or s == 5 or s == 7) and t % 2 == 0:
                first_num = f
                second_num = s
                third_num = t
                print(f"{first_num} {second_num} {third_num}")
