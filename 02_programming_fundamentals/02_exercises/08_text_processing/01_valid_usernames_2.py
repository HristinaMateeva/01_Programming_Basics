usernames = input().split(", ")

is_length_valid = False
is_alnum_valid = False

for user_id in usernames:
    if 3 <= len(user_id) <= 16:
        is_length_valid = True
    else:
        is_length_valid = False
    if user_id.isalnum() or "-" in user_id or "_" in user_id:
        is_alnum_valid = True
    else:
        is_alnum_valid = False

    if is_length_valid and is_alnum_valid:
        print(user_id)
