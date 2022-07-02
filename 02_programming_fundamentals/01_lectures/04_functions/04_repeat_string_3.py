def repeat_string(string, repeat):
    result = ""
    for i in range(1, num + 1):
        result += string
    return result


input_string = input()
num = int(input())

print(repeat_string(input_string, num))
