def length_is_valid(f_username):
    if 3 <= len(f_username) <= 16:
        return True
    return False


def characters_are_valid(f_username):
    for char in f_username:
        if not (char.isalnum() or char == "-" or char == "_"):
            return False
    return True


def no_redundant_symbols(f_username):
    if " " in f_username:
        return False
    return True


def username_is_valid(f_username):
    if length_is_valid(f_username) and characters_are_valid(f_username) and no_redundant_symbols(f_username):
        return True
    return False


usernames = input().split(", ")

for username in usernames:
    if username_is_valid(username):
        print(username)
