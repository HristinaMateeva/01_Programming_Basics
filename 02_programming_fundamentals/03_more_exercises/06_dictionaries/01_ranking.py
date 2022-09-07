def is_valid_contest(f_initial_contest_data, f_contest, f_password):
    if f_contest not in f_initial_contest_data:
        return False
    elif not f_initial_contest_data[f_contest] == f_password:
        return False
    return True


initial_command = input()

initial_contest_data = {}
final_contest_data = {}
results = {}
total_points_students = {}
final_results = {}

while not initial_command == "end of contests":
    contest, password = initial_command.split(":")
    initial_contest_data[contest] = password
    initial_command = input()

command = input()

while not command == "end of submissions":
    contest, password, username, points = command.split("=>")
    points = int(points)
    if is_valid_contest(initial_contest_data, contest, password):
        if contest not in final_contest_data:
            final_contest_data[contest] = {username: points}
        else:
            if username not in final_contest_data[contest] or final_contest_data[contest][username] < points:
                final_contest_data[contest][username] = points
    command = input()

for course, students in final_contest_data.items():
    for student, result in students.items():
        if student not in results:
            results[student] = {course: result}
        else:
            results[student][course] = result
        if student not in total_points_students:
            total_points_students[student] = result
        else:
            total_points_students[student] += result

for user, course_id in results.items():
    final_results[user] = dict(sorted(course_id.items(), key=lambda kvp: kvp[1], reverse=True))

final_results = dict(sorted(final_results.items(), key=lambda kvp: (kvp[0], kvp[1])))
total_points_students = dict(sorted(total_points_students.items(), key=lambda kvp: kvp[1], reverse=True))

for key, value in total_points_students.items():
    print(f"Best candidate is {key} with total {value} points.")
    break

print("Ranking:")

for user_id, contents_id in final_results.items():
    print(user_id)
    for content_id, final_points in contents_id.items():
        print(f"#  {content_id} -> {final_points}")
