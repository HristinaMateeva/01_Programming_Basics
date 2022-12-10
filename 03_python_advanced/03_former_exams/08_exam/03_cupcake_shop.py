from collections import deque


def stock_availability(inventory, *args):
    inventory = deque(inventory)
    action = args[0]
    if action == "delivery":
        inventory.extend(args[1:])
    elif action == "sell":
        if len(args) == 1:
            inventory.popleft()
        elif type(args[1]) == int:
            number = int(args[1])
            for num in range(number):
                inventory.popleft()
        else:
            products = args[1:]
            for product in products:
                while product in inventory:
                    inventory.remove(product)
    return list(inventory)


# ------------------------------
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# ------------------------------
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# ------------------------------
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# ------------------------------
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# ------------------------------
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# ------------------------------
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# ------------------------------
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
