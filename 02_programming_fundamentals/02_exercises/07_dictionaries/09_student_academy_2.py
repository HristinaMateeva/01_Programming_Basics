num_lines = int(input())

all_grades = {}
average_grades = {}

for num in range(1, num_lines + 1):
    name = input()
    grade = float(input())
    if name in all_grades:
        all_grades[name] += [grade]
    else:
        all_grades[name] = [grade]

for key, value in all_grades.items():
    if key in average_grades:
        average_grades[key] += sum(value) / len(value)
    else:
        average_grades[key] = sum(value) / len(value)

for names, av_grade in average_grades.items():
    if av_grade >= 4.50:
        print(f"{names} -> {av_grade:.2f}")
