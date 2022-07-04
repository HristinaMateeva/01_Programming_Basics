def sort_func(sequence):
    sequence.sort()
    return sequence


sequence_of_numbers = input().split()
sequence_of_numbers = [int(el) for el in sequence_of_numbers]

print(sort_func(sequence_of_numbers))
