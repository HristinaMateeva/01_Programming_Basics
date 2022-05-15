number_jury = int(input())
presentation_name = input()

counter_presentations = 0
sum_average_grades_all_students = 0
total_average = 0
average_per_student = 0

while presentation_name != "Finish":
    all_grades_per_presentation = 0
    counter_presentations += 1
    for number in range(1, number_jury + 1):
        grade = float(input())
        all_grades_per_presentation += grade
        average_per_student = all_grades_per_presentation / number
    print(f"{presentation_name} - {average_per_student:.2f}.")
    sum_average_grades_all_students += average_per_student
    total_average = sum_average_grades_all_students / counter_presentations

    presentation_name = input()
print(f"Student's final assessment is {total_average:.2f}.")
