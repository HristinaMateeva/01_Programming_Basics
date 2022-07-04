def palindrome_integers(nums):
    for element in nums:
        if element == element[::-1]:
            print(True)
        else:
            print(False)


numbers = input().split(", ")

palindrome_integers(numbers)
