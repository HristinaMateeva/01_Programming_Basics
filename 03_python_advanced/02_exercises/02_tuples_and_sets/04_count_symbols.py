line = input()
chars_counts = {}

for char in line:
    if char in chars_counts:
        chars_counts[char] += 1
    else:
        chars_counts[char] = 1

for x in sorted(chars_counts.items()):
    print(f"{x[0]}: {x[1]} time/s")
