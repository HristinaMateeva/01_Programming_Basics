n = int(input())

stack = []

for _ in range(n):
    command = input().split()
    if command[0] == "1":
        stack.append(int(command[1]))
    elif command[0] == "2" and stack:
        stack.pop()
    elif command[0] == "3" and stack:
        print(max(stack))
    elif command[0] == "4" and stack:
        print(min(stack))

reversed_stack = stack[::-1]
print(', '.join(str(el) for el in reversed_stack))
