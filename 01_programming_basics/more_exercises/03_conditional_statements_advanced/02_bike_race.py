num_juniors = int(input())
num_seniors = int(input())
type_trace = input()
sum = 0
total_num = 0
if type_trace == "trail":
    sum = num_juniors * 5.50 + num_seniors * 7
elif type_trace == "cross-country":
    sum = num_juniors * 8 + num_seniors * 9.50
    total_num = num_juniors + num_seniors
    if total_num >= 50:
        sum *= 0.75
elif type_trace == "downhill":
    sum = num_juniors * 12.25 + num_seniors * 13.75
elif type_trace == "road":
    sum = num_juniors * 20 + num_seniors * 21.50
sum *= 0.95
print(f"{sum:.2f}")
