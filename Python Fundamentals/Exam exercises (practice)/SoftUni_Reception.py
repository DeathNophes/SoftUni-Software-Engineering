employee1_efficiency = int(input())
employee2_efficiency = int(input())
employee3_efficiency = int(input())
students_count = int(input())

students_per_hour = employee1_efficiency + employee2_efficiency + employee3_efficiency

break_count = 0
hour = 0
while students_count > 0:
    if break_count == 3:
        break_count = 0
        hour += 1
        continue

    students_count -= students_per_hour
    hour += 1
    break_count += 1

print(f"Time needed: {hour}h.")
