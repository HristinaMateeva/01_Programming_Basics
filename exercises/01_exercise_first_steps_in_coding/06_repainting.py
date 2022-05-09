nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
materials_sum = (nylon + 2) * 1.50 + \
                paint * 1.1 * 14.50 + \
                thinner * 5 + \
                0.40
salary = materials_sum * 0.3 * hours
total_sum = materials_sum + salary
print(total_sum)
