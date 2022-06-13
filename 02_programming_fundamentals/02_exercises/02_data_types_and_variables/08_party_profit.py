companions = int(input())
days = int(input())

total_coins = 0

for num in range(1, days + 1):
    if num % 10 == 0:
        companions -= 2
    if num % 15 == 0:
        companions += 5
    if num % 3 == 0:
        total_coins -= (companions * 3)
    if num % 5 == 0:
        total_coins += (companions * 20)
        if num % 3 == 0:
            total_coins -= (companions * 2)
    total_coins += 50
    total_coins -= companions * 2

average_coins = int(total_coins / companions) # it can be written as average_coins = total_coins // party_size
print(f"{companions} companions received {average_coins} coins each.")
