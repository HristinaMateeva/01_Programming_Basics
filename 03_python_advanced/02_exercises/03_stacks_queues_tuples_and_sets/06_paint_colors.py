from collections import deque

main_colours = {"red", "yellow", "blue"}
secondary_colours = {"orange", "purple", "green"}

substrings = deque(input().split())
collected_colours = list()

while substrings:
    first_substring = substrings.popleft()
    second_substring = substrings.pop() if substrings else ''

    result = first_substring + second_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    result = second_substring + first_substring
    if result in main_colours or result in secondary_colours:
        collected_colours.append(result)
        continue

    first_substring = first_substring[:-1]
    second_substring = second_substring[:-1]

    if first_substring:
        substrings.insert(len(substrings) // 2, first_substring)
    if second_substring:
        substrings.insert(len(substrings) // 2, second_substring)

result = []
required_colours = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

for colour in collected_colours:
    if colour in main_colours:
        result.append(colour)
    else:
        is_valid = True
        for required_colour in required_colours[colour]:
            if required_colour not in collected_colours:
                is_valid = False
                break
        if is_valid:
            result.append(colour)

print(result)
