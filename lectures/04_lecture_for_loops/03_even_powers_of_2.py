# import math
n = int(input())

for power in range(0, n + 1, 2):
    # print(math.pow(2, power)) - Функция от math за повдигане на степен
    print(2 ** power)
