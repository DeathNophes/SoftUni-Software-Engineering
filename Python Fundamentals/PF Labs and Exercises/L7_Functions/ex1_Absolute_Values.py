numbers = input().split()
absolute_values = []
for number in numbers:
    absolute_values.append(abs(float(number)))
    # Превръщаме го в float
print(absolute_values)