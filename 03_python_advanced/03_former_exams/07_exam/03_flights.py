def flights(*args):
    result = {}
    for index in range(0, len(args), 2):
        if args[index] == "Finish":
            return result
        destination = args[index]
        count_passengers = int(args[index + 1])
        if destination not in result:
            result[destination] = count_passengers
        else:
            result[destination] += count_passengers
    return result


# ------------------------------
print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# ------------------------------
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# ------------------------------
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
