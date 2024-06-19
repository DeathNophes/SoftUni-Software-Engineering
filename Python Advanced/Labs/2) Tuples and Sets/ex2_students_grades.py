n = int(input())
students = {}
for _ in range(n):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

for key, value in students.items():
    formatted_grades = " ".join([f"{grade:.2f}" for grade in value])
    avg = sum(value) / len(value)
    print(f"{key} -> {formatted_grades} (avg: {avg:.2f})")
