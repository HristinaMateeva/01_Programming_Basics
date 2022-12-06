from helpers import locate, create_sequence


def run_fib():
    data = input()
    sequence = []
    while not data == "Stop":
        split_data = data.split()
        if split_data[0] == "Create":
            number = int(split_data[-1])
            sequence = create_sequence(number)
            print(*sequence)
        elif split_data[0] == "Locate":
            number = int(split_data[-1])
            locate(sequence, number)
        data = input()
