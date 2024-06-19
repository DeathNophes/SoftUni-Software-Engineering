students = []
searched_course = None

line = input()
while True:
    if ':' not in line:
        searched_course = line
        break
    name, ID, course = line.split(":")
    ID = int(ID)
    students.append({'name': name, 'ID': ID, 'course': course})
    line = input()

for student in students:
    if searched_course.startswith(student['course'][0:3]):
        #   We use this method, because judge gives 'searched_course'
        #   with the same meaning but different symbols.
        print(f"{student['name']} - {student['ID']}")
