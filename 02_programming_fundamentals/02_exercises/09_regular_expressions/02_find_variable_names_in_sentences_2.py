import re

data = input()
pattern = r"\b_[a-zA-Z0-9]+\b"

matches = re.findall(pattern, data)
result = ','.join(matches)

print(result.replace('_', ''))
