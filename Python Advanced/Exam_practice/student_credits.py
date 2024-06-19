def students_credits(*args):
    result = ""
    grades = {}
    total_credits = 0

    for el in args:
        course_name, course_credits, max_points, points = el.split('-')
        earned_percent_of_max_points = int(points) / int(max_points)
        earned_credits = float(earned_percent_of_max_points) * int(course_credits)
        grades[course_name] = earned_credits

    for curr_credits in grades.values():
        total_credits += curr_credits

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        diff = 240 - total_credits
        result += f"Diyan needs {diff:.1f} credits more for a diploma.\n"

    for course, course_credits in sorted(grades.items(), key=lambda x: -x[1]):
        result += f"{course} - {course_credits:.1f}\n"

    return result
