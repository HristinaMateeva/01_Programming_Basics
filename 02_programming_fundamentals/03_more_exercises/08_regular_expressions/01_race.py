import re

names = input().split(", ")
command = input()

pattern_name = r"[A-Za-z]"
patern_digits = r"[0-9]"

valid_names = {}
final_result = {}
counter = 0

while not command == "end of race":
    matches_names = re.finditer(pattern_name, command)
    matches_digits = [int(num) for num in re.findall(patern_digits, command)]
    current_sequence = ""
    for match in matches_names:
        match = match.group()
        current_sequence += match
    if current_sequence not in valid_names and current_sequence in names:
        valid_names[current_sequence] = sum(matches_digits)
    elif current_sequence in valid_names and current_sequence in names:
        valid_names[current_sequence] += sum(matches_digits)
    command = input()

valid_names = dict(sorted(valid_names.items(), key=lambda kvp: -kvp[1]))

for name, kilometers in valid_names.items():
    counter += 1
    final_result[name] = kilometers
    if counter == 1:
        print(f"1st place: {name}")
    elif counter == 2:
        print(f"2nd place: {name}")
    elif counter == 3:
        print(f"3rd place: {name}")
        break
