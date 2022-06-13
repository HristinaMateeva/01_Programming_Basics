num_snowballs = int(input())

max_snowball_value = 0
max_snowball_snow = 0
max_snowball_time = 0
max_snowball_quality = 0

for num in range(1, num_snowballs + 1):
    current_snowball_snow = int(input())
    current_snowball_time = int(input())
    current_snowball_quality = int(input())
    current_snowball_value = (current_snowball_snow / current_snowball_time) ** current_snowball_quality
    if current_snowball_value > max_snowball_value:
        max_snowball_value = current_snowball_value
        max_snowball_snow = current_snowball_snow
        max_snowball_time = current_snowball_time
        max_snowball_quality = current_snowball_quality

print(f"{max_snowball_snow} : {max_snowball_time} = {int(max_snowball_value)} ({max_snowball_quality})")
