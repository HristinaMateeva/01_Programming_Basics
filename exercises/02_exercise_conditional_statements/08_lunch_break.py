import math

name_series = str(input())
duration_episode = int(input())
duration_break = int(input())
duration_lunch = duration_break / 8
duration_rest = duration_break / 4
left_time = duration_break - duration_lunch - duration_rest
needed_time = abs(left_time - duration_episode)
if left_time >= duration_episode:
    print(f"You have enough time to watch {name_series} and left with {math.ceil(needed_time)} \
minutes free time.")
else:
    print(f"You don't have enough time to watch {name_series}, you need {math.ceil(needed_time)} more \
minutes.")
