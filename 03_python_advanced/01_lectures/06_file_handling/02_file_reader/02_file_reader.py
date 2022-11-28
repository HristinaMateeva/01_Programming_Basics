# try:
#     with open("numbers.txt") as file:
#         print(sum([int(line_sum) for line_sum in file.readlines()]))
#         # result = 0
#         # for line in file.readlines():
#         #     current_num = int(line)
#         #     result += current_num
#         # print(result)
# except FileNotFoundError:
#     print("File was not found")

with open("numbers.txt") as file:
    for line in file:
        print(line)