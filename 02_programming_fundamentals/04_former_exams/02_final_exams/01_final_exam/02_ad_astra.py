import re

text = input()
pattern = r"(#|\|)(?P<Item>[a-zA-Z\s]+)\1(?P<Date>\d{2}/\d{2}/\d{2})\1(?P<Calories>\d+)\1"

calories_per_day = 2000
matches = re.finditer(pattern, text)
total_calories = [int(match.group(4)) for match in re.finditer(pattern, text)]
days_enough_food = sum(total_calories) // calories_per_day

print(f"You have food to last you for: {days_enough_food} days!")

for match in matches:
    data = match.groupdict()
    print(f"Item: {data['Item']}, Best before: {data['Date']}, Nutrition: {data['Calories']}")
