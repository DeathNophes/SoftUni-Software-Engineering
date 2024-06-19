courses = {}

command = input()
while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in courses.keys():
        courses[course_name] = [student_name]   # We create a list with the student name in it
    else:
        courses[course_name].append(student_name)   # We add to the current list
    command = input()

for curr_course in courses.keys():
    students = len(courses[curr_course])    # Length of the list
    print(f"{curr_course}: {students}")
    for name in courses[curr_course]:
        print(f"-- {name}")
