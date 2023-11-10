exams = {}
submissions = {}

command = input()
while command != "exam finished":
    if 'banned' in command:
        command = command.split('-')
        username = command[0]
        del exams[username]
        command = input()
        continue

    username, language, points = command.split('-')
    points = int(points)

    if language not in submissions.keys():
        submissions[language] = 0
    submissions[language] += 1

    if username not in exams.keys():
        exams[username] = [language, points]
    else:
        if language in exams[username]:
            index = exams[username].index(language)
            if exams[username][index + 1] < points:
                exams[username][index + 1] = points
        else:
            exams[username].append(language)
            exams[username].append(points)

    command = input()

print("Results: ")
for key, value in exams.items():
    print(f"{key} | {value[1]}")
print("Submissions: ")
for key, value in submissions.items():
    print(f"{key} - {value}")
