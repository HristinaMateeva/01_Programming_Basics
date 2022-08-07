command = input()

language_submissions = {}
final_results = {}

while not command == "exam finished":
    if "banned" in command:
        command = command.split("-")
        banned_user = command[0]
        final_results.pop(banned_user)
    else:
        username, language, points = command.split("-")
        points = int(points)
        if language not in language_submissions:
            language_submissions[language] = 1
        else:
            language_submissions[language] += 1
        if username not in final_results or points > final_results[username]:
            final_results[username] = points
    command = input()

print("Results:")
for user, points in final_results.items():
    print(f"{user} | {points}")
print("Submissions:")
for lang, counter in language_submissions.items():
    print(f"{lang} - {counter}")
