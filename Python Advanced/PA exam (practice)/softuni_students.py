def softuni_students(*args, **kwargs):
    valid_students = []
    invalid_students = []

    for course_id, username in sorted(args, key=lambda x: x[1]):
        if course_id in kwargs:
            valid_students.append((course_id, username))
        else:
            invalid_students.append(username)

    result = ''
    for student in valid_students:
        result += f"*** A student with the username {student[1]} " \
                  f"has successfully finished the course {kwargs[student[0]]}!\n"

    if invalid_students:
        result += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return result
