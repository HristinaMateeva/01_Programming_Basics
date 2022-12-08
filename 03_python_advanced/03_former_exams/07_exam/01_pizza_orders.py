from collections import deque


def validation_data(order):
    if 0 < order <= 10:
        return True
    return False


pizzas_orders = deque([int(el) for el in input().split(", ")])
employees = [int(el) for el in input().split(", ")]

total_pizzas = 0

while pizzas_orders and employees:
    current_order = pizzas_orders.popleft()

    if not validation_data(current_order):
        continue

    current_employee = employees.pop()
    if current_employee >= current_order:
        total_pizzas += current_order
    else:
        current_order -= current_employee
        total_pizzas += current_employee
        pizzas_orders.appendleft(current_order)

if not pizzas_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(el) for el in employees])}")
elif not employees and pizzas_orders:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(el) for el in pizzas_orders])}")
