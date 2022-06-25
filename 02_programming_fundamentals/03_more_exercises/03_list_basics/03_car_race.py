sequence = [int(el) for el in input().split()]

racer_1 = []
racer_2 = []
sum_racer_1 = 0
sum_racer_2 = 0
half = len(sequence) // 2

#Racer 1
for index in range(half):
    racer_1.append(sequence[index])
    if not sequence[index] == 0:
        sum_racer_1 += sequence[index]
    else:
        sum_racer_1 *= 0.8

#Racer 2
for index in range(len(sequence) - 1, half, -1):
    racer_2.append(sequence[index])
    if not sequence[index] == 0:
        sum_racer_2 += sequence[index]
    else:
        sum_racer_2 *= 0.8

if sum_racer_1 < sum_racer_2:
    print(f"The winner is left with total time: {sum_racer_1:.1f}")
else:
    print(f"The winner is right with total time: {sum_racer_2:.1f}")
