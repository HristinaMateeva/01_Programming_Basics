import re

data = input()
searched = input()

# pattern = f"\\b{searched}\\b"
pattern = fr"\b{searched}\b"

result = re.findall(pattern, data, re.IGNORECASE)
print(len(result))
