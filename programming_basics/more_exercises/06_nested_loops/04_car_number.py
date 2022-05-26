first_num = int(input())
last_num = int(input())

is_valid = True

for i in range(first_num, last_num + 1):
    for j in range(first_num, last_num + 1):
        for k in range(first_num, last_num + 1):
            for l in range(first_num, last_num + 1):
                sum = j + k
                if i % 2 == 0 and l % 2 == 1 and i > l and sum % 2 == 0:
                    print(f"{i}{j}{k}{l}", end= " ")
                elif i % 2 == 1 and l % 2 == 0 and i > l and sum % 2 == 0:
                    print(f"{i}{j}{k}{l}", end= " ")
                else:
                    is_valid = False
                    continue
