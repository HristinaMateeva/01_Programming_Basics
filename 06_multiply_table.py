# abc
number = int(input())

a = number // 100 % 10  # стотици
b = number // 10 % 10  # десетици
c = number % 10  # единици

for i in range(1, c +1):
    for j in range(1, b + 1):
        for k in range (1, a +1):
            multiplication = i * j * k
            print(f"{i} * {j} * {k} = {multiplication};")
