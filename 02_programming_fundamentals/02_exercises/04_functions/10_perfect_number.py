def perfect_number(num):
    divisors = []
    for n in range(1, (num // 2) + 1):
        if num % n == 0:
            divisors.append(n)
    if sum(divisors) == num:
        return True
    return False


number = int(input())
if perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
