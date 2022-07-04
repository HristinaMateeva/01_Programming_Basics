def password_validator(received_password):
    counter_digits = 0
    is_valid = True
    if 6 > len(received_password) < 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")
    if not received_password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")
    for el in received_password:
        if el.isdigit():
            counter_digits += 1
    if counter_digits < 2:
        is_valid = False
        print("Password must have at least 2 digits")
    if is_valid:
        print("Password is valid")


password = input()

password_validator(password)
