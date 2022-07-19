substrings = input().split(", ")
words = input().split(", ")

result = [subst for subst in substrings for word in words if subst in word]

print(sorted(set(result), key=result.index))
