def even_numbers(sequence):
    result = []
    for num in sequence:
        if num % 2 == 0:
            result.append(num)
    return result


sequence_of_numbers = input().split()
sequence_of_numbers_as_int = [int(el) for el in sequence_of_numbers]

print(even_numbers(sequence_of_numbers_as_int))
