start_range = int(input())
end_range = int(input())

for index in range(start_range, end_range + 1):
    character = chr(index)
    print(f"{character}", end=" ")
