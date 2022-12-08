from collections import deque

bowls_ramen = [int(el) for el in input().split(", ")]
customers = deque([int(el) for el in input().split(", ")])

while bowls_ramen and customers:
    current_bowl = bowls_ramen[-1]
    current_customer = customers[0]
    if current_bowl == current_customer:
        bowls_ramen.pop()
        customers.popleft()
    elif current_bowl > current_customer:
        bowls_ramen[-1] -= current_customer
        customers.popleft()
    elif current_customer > current_bowl:
        customers[0] -= current_bowl
        bowls_ramen.pop()

if not customers:
    print("Great job! You served all the customers.")
    if bowls_ramen:
        print(f"Bowls of ramen left: {', '.join([str(el) for el in bowls_ramen])}")
elif not bowls_ramen:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(el) for el in customers])}")
