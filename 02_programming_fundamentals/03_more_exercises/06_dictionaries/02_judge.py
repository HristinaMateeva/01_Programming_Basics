command = input()

contest_data = {}
individual_statistics = {}
total_points_per_student = {}

while not command == "no more time":
    username, contest, points = command.split(" -> ")
    points = int(points)
    if contest not in contest_data:
        contest_data[contest] = {username: points}
    elif username not in contest_data[contest] or contest_data[contest][username] < points:
        contest_data[contest][username] = points
    if username not in individual_statistics:
        individual_statistics[username] = {contest: points}
    elif contest not in individual_statistics[username] or individual_statistics[username][contest] < points:
        individual_statistics[username][contest] = points

    command = input()

for contest_id, username_id in contest_data.items():
    contest_data[contest_id] = dict(sorted(username_id.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for user_id, courses_id in individual_statistics.items():
    individual_statistics[user_id] = dict(sorted(courses_id.items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for course_id, current_points in courses_id.items():
        if user_id not in total_points_per_student:
            total_points_per_student[user_id] = current_points
        else:
            total_points_per_student[user_id] += current_points

total_points_per_student = dict(sorted(total_points_per_student.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for course, names in contest_data.items():
    print(f"{course}: {len(contest_data[course])} participants")
    counter = 0
    for name, results in names.items():
        counter += 1
        print(f"{counter}. {name} <::> {results}")

counter = 0
print("Individual standings:")
for student_name, result in total_points_per_student.items():
    counter += 1
    print(f"{counter}. {student_name} -> {result}")
