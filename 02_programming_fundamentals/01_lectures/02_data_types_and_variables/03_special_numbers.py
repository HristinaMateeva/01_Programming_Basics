number = int(input())

for num in range(1, number + 1):
    result = 0
    num_as_str = str(num)
    for char in num_as_str:
        result += int(char)
    if result == 5 or result == 7 or result == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
