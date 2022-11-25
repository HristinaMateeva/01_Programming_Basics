def age_assignment(*args, **kwargs):
    current_result = {}
    result = ""
    args = tuple(sorted(args, key=lambda x: x))
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        current_result[name] = age
        result += f"{name} is {age} years old." + '\n'
    return result


# ------------------------------
print(age_assignment("Peter", "George", G=26, P=19))
# ------------------------------
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
