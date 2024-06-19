def is_even(number):
    return number % 2 == 0
    # Връща True или False


numbers_as_str = input().split()
numbers_as_int = []
for digit in numbers_as_str:
    numbers_as_int.append(int(digit))
even_numbers = []
for element in numbers_as_int:
    if is_even(element):
        even_numbers.append(element)
print(even_numbers)
