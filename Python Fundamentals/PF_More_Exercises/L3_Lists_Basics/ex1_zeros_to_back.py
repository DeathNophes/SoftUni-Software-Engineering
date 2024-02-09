numbers = input().split(", ")
numbers_as_int = []
zeros = numbers.count("0")
while "0" in numbers:
    numbers.remove("0")
for _ in range(zeros):
    numbers.append("0")
for number in numbers:
    numbers_as_int.append(int(number))
print(numbers_as_int)
