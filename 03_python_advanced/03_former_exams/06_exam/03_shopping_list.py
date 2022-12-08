def shopping_list(budget, **kwargs):
    products_dict = {}
    result = ""

    if budget < 100:
        return "You do not have enough budget."

    for type_product, details in kwargs.items():
        if len(products_dict) >= 5:
            return result
        product = type_product
        price_per_each = float(details[0])
        quantity = int(details[1])
        price_product = price_per_each * quantity
        if price_product <= budget:
            products_dict[product] = price_product
            budget -= price_product
            result += f"You bought {product} for {price_product:.2f} leva.\n"
        else:
            continue
    return result


# ------------------------------
print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))
# ------------------------------
print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))
# ------------------------------
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
