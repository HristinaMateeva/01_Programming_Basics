import random

# number = random.randint(1, 3)
# guess_number = int(input("Enter the number between 1 to 3: "))
# if guess_number == number:
#     print("Successful choice")

# ascii_value = random.randint(65, 90)
# letter = chr(ascii_value)
# print(letter)

questions = ["Кога е основана България?", "Колко е 2 * 2?", "Коя е най-голямата по площ държава в Света?"]
guess_counter = 0
answered_questions = []

for _ in range(10):
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue

    if current_question == "Кога е основана България?":
        answer = input("Моля въведете отговор: ")
        if answer == "681":
            print("Ти позна въпроса!")
            guess_counter += 1
        else:
            print("Грешен отговор!")

    elif current_question == "Колко е 2 * 2?":
        answer = input("Моля въведете отговор: ")
        if answer == "4":
            print("Ти позна въпроса!")
            guess_counter += 1
        else:
            print("Грешен отговор!")

    elif current_question == "Коя е най-голямата по площ държава в Света?":
        answer = input("Моля въведете отговор: ")
        if answer == "Русия":
            print("Ти позна въпроса!")
            guess_counter += 1
        else:
            print("Грешен отговор!")
