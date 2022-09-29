import re

number = int(input())
pattern_data = r"\|(?P<boss>[A-Z]{4,})\|:#(?P<title>[A-Za-z]+\s[A-Za-z]+)#"

for num in range(number):
    input_data = input()
    match_data = re.finditer(pattern_data, input_data)
    valid_data = re.findall(pattern_data, input_data)
    strength = 0
    armor = 0
    if valid_data:
        for match in match_data:
            data_dict = match.groupdict()
            strength = len(data_dict['boss'])
            armor = len(data_dict['title'])
            print(f"{data_dict['boss']}, The {data_dict['title']}")
            print(f">> Strength: {strength}")
            print(f">> Armor: {armor}")
    else:
        print("Access denied!")
