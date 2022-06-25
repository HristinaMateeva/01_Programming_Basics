sequence = [int(el) for el in input().split()]

racer_1 = []
racer_2 = []
sum_racer_1 = 0
sum_racer_2 = 0
half = len(sequence) // 2


def time_calculation(beginning_index, end_index, step, racer_list, sum_racer):
    for index in range(beginning_index, end_index, step):
        racer_list.append(sequence[index])
        if not sequence[index] == 0:
            sum_racer += sequence[index]
        else:
            sum_racer *= 0.8
    return sum_racer


sum_racer_1 = time_calculation(0, half, 1, racer_1, sum_racer_1)
sum_racer_2 = time_calculation((len(sequence) - 1), half, -1, racer_2, sum_racer_2)

if sum_racer_1 < sum_racer_2:
    print(f"The winner is left with total time: {sum_racer_1:.1f}")
else:
    print(f"The winner is right with total time: {sum_racer_2:.1f}")
