expression = input()

stack = []

for index in range(len(expression)):
    char = expression[index]
    if char == "(":
        stack.append(index)
    elif char == ")":
        last_opening_bracket_index = stack.pop()
        sub_expression = expression[last_opening_bracket_index:index + 1]
        print(sub_expression)
