numbers = [int(el) for el in input().split()]

positive_numbers = sum([x for x in numbers if x > 0])
negative_numbers = sum([x for x in numbers if x < 0])

print(negative_numbers)
print(positive_numbers)

if abs(positive_numbers) > abs(negative_numbers):
    print("The positives are stronger than the negatives")
elif abs(positive_numbers) < abs(negative_numbers):
    print("The negatives are stronger than the positives")
