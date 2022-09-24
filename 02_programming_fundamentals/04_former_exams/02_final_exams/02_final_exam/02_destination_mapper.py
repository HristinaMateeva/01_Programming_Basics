import re

text = input()
pattern = r"(=|/)(?P<destination>[A-Z][a-zA-Z]{2,})\1"

total_points = 0
destination_data = []
matches = re.finditer(pattern, text)

for match in matches:
    object_dict = match.groupdict()
    destination_data.append(object_dict['destination'])
    total_points += len(object_dict['destination'])

print(f"Destinations: {', '.join(destination_data)}")
print(f"Travel Points: {total_points}")
