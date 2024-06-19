grades = {}
n = int(input())

for _ in range(n):
    student_name = input()
    curr_grade = float(input())

    if student_name not in grades.keys():
        grades[student_name] = [curr_grade]
    else:
        grades[student_name].append(curr_grade)

for student in grades.keys():
    avg_grade = sum(grades[student]) / len(grades[student])
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")
