first_sequence = set([int(el) for el in input().split()])
second_sequence = set([int(el) for el in input().split()])

number = int(input())

for num in range(number):
    command = input().split()
    if command[0] == "Add":
        new_sequence = set([int(el) for el in command[2:]])
        if command[1] == "First":
            first_sequence.union(new_sequence)
        elif command[2] == "Second":
            second_sequence.union(new_sequence)
    elif command[0] == "Remove":
        new_sequence = set([int(el) for el in command[2:]])
        if command[1] == "First":
            first_sequence = first_sequence.difference(new_sequence)
        elif command[1] == "Second":
            second_sequence = second_sequence.difference(new_sequence)
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
