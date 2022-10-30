from collections import deque

elements = input().split()
numbers = deque()

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a // b
}

for element in elements:
    # element is operator
    if element in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = operations[element](first, second)
            numbers.appendleft(result)
    # element is number
    else:
        numbers.append(int(element))

print(numbers.popleft())
