from functools import reduce


def operate(sign, *args):
    try:
        return reduce(lambda x, y: eval(f"{x} {sign} {y}"), args)
    except ZeroDivisionError:
        print("Invalid arguments - zero included...")
        return reduce(lambda x, y: eval(f"{x} {sign} {y}"), [el for el in args if el != 0])

# ------------------------------
# print(operate("+", 1, 2, 3))
# ------------------------------
# print(operate("*", 3, 4))
