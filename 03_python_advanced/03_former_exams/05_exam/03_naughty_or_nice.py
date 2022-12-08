def naughty_or_nice_list(kids_list, *args, **kwargs):
    # current_list = {"name": {"number": 0, "classification": ''}}
    current_list = {}
    final_result = {"Nice": [], "Naughty": [], "Not found": []}
    for kids_tuple in kids_list:
        kid_number = int(kids_tuple[0])
        kid_name = kids_tuple[1]
        current_list[kid_name] = {"number": kid_number}
    if args:
        for el in args:
            num, class_kid = el.split('-')
            num = int(num)

    if kwargs:
        pass


# ------------------------------
print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))

# Not ready