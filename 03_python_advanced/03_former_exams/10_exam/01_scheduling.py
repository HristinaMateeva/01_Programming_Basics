from sys import maxsize

jobs = [int(el) for el in input().split(", ")]
index = int(input())

clock_cycles = 0

while True:
    min_number = min(jobs)
    min_number_index = jobs.index(min_number)
    clock_cycles += min_number
    jobs[min_number_index] -= min_number
    if jobs[index] == 0:
        print(clock_cycles)
        break
    else:
        jobs[min_number_index] = maxsize
