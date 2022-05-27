import math

command = input()

current_most_powerful_word = " "
max_points = 0
points_current_word = 0
type_calculation = " "

while command != "End of words":
    sum_current_word = 0
    word = command
    length_word = len(word)
    for letter in word:
        letter_amount = ord(letter)
        sum_current_word += letter_amount
        if word[0] == chr(65) or word[0] == chr(69) or word[0] == chr(73) or word[0] == chr(79) or word[0] == chr(85) or \
                word[0] == chr(89) or word[0] == chr(97) or word[0] == chr(101) or word[0] == chr(105) or word[
            0] == chr(111) or word[0] == chr(117) or word[0] == chr(121):
            type_calculation = "variant1"
        else:
            type_calculation = "variant2"
    if type_calculation == "variant1":
        points_current_word = sum_current_word * length_word
    else:
        points_current_word = math.floor(sum_current_word / length_word)
    if points_current_word > max_points:
        max_points = points_current_word
        current_most_powerful_word = word
    command = input()

print(f"The most powerful word is {current_most_powerful_word} - {max_points}")
