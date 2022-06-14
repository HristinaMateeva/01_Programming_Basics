num_lines = int(input())

bracket_list = ["(", ")"]
is_balanced = True
last_bracket = ""

for num in range(num_lines):
    command = input()
    if command not in bracket_list:
        continue

    if (last_bracket == '' and command == ')') or last_bracket == command:
        is_balanced = False
        break
    last_bracket = command

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
