import re

pattern = r"\s[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-zA-Z-]+\.[a-zA-z-]+[\.]?[a-zA-z]+\b"
data = input()

matches = re.findall(pattern, data)
result = ""
for el in matches:
    # print(''.join(el).strip()) without result variable
    result = ''.join(el)
    print(result.strip())
