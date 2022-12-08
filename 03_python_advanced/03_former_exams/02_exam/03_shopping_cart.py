def shopping_cart(*args):
    food_limits = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    received_items = {"Soup": [], "Pizza": [], "Dessert": []}
    final_result = ""

    for arg in args:
        if arg == "Stop":
            break
        type_meal = arg[0]
        product = arg[1]

        if food_limits[type_meal] <= len(received_items[type_meal]):
            continue

        # if type_meal not in received_items:
        #     received_items[type_meal] = []
        #     received_items[type_meal].append(product)
        if product not in received_items[type_meal]:
            received_items[type_meal].append(product)

    sorted_result = dict(sorted(received_items.items(), key=lambda x: (-len(x[1]), x[0])))

    if not received_items["Soup"] and not received_items["Pizza"] and not received_items["Dessert"]:
        final_result = "No products in the cart!"
        return final_result
    for meal, products in sorted_result.items():
        products.sort()
        final_result += f"{meal}:\n"
        for type_product in products:
            final_result += f" - {type_product}\n"
    return final_result


# ------------------------------
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))
# ------------------------------
print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))
# ------------------------------
print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
