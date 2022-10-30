from collections import deque

chocolates_as_stack = [int(el) for el in input().split(', ')]
cups_of_milk = deque(int(el) for el in input().split(', '))

milkshakes = 0
enough_milkshakes = False

while chocolates_as_stack and cups_of_milk:
    if chocolates_as_stack[-1] <= 0:
        chocolates_as_stack.pop()
    elif cups_of_milk[0] <= 0:
        cups_of_milk.popleft()
    elif chocolates_as_stack[-1] == cups_of_milk[0]:
        chocolates_as_stack.pop()
        cups_of_milk.popleft()
        milkshakes += 1
    else:
        chocolates_as_stack[-1] -= 5
        cups_of_milk.append(cups_of_milk.popleft())
    if milkshakes == 5:
        enough_milkshakes = True
        break

if enough_milkshakes:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates_as_stack:
    print(f"Chocolate: {', '.join(str(el) for el in chocolates_as_stack)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(el) for el in cups_of_milk)}")
else:
    print("Milk: empty")

# 92% in Judge
