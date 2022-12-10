from collections import deque


def special_case(f_males, f_females):
    if f_males[-1] % 25 == 0:
        f_males.pop()
        f_males.pop()
    if f_females[0] % 25 == 0:
        f_females.popleft()
        f_females.popleft()
    return f_males, f_females


males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

matches = 0

while males and females:
    males, females = special_case(males, females)
    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0:
        females.appendleft(current_female)
        continue
    if current_female <= 0:
        males.append(current_male)
        continue

    if current_male == current_female:
        matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(el) for el in males])}")
else:
    print("Males left: none")
if females:
    print(f"Females left: {', '.join([str(el) for el in females])}")
else:
    print("Females left: none")

# Not ready
