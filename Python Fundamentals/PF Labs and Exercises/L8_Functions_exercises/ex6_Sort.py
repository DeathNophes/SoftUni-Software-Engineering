def sorted_numbers(some_numbers: list):
    numbers_as_int = []
    for number in some_numbers:
        numbers_as_int.append(int(number))
    numbers_as_int.sort(reverse=False)
    return numbers_as_int


numbers = input().split()
print(sorted_numbers(numbers))