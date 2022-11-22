def negative_vs_positive(*args):
    nums = [int(el) for el in args[0].split()]
    positive_nums = [el for el in nums if el > 0]
    negative_nums = [el for el in nums if el < 0]
    return positive_nums, negative_nums


numbers = input()

positive_numbers, negative_numbers = negative_vs_positive(numbers)

print(sum(negative_numbers))
print(sum(positive_numbers))

if abs(sum(positive_numbers)) > abs(sum(negative_numbers)):
    print("The positives are stronger than the negatives")
elif abs(sum(positive_numbers)) < abs(sum(negative_numbers)):
    print("The negatives are stronger than the positives")
