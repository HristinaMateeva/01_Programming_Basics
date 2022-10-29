from collections import deque

expression = input().split()

current_sequence = deque()
result = ""

for el in expression:
    current_result = result
    if el.lstrip("-").isdigit():
        current_sequence.append(int(el))
    else:
        if result == "":
            result = current_sequence.popleft()
        else:
            result = current_result
        while current_sequence:
            if el == "+":
                result += current_sequence.popleft()
            elif el == "-":
                result -= current_sequence.popleft()
            elif el == "*":
                result *= current_sequence.popleft()
            elif el == "/":
                result //= current_sequence.popleft()

print(result)
