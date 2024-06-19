def positive(some_numbers: list):
    positive_nums = [digit for digit in some_numbers if int(digit) >= 0]
    return ", ".join(positive_nums)


def negative(some_numbers: list):
    negative_nums = [digit for digit in some_numbers if int(digit) < 0]
    return ", ".join(negative_nums)


def even(some_numbers: list):
    even_nums = [digit for digit in some_numbers if int(digit) % 2 == 0]
    return ", ".join(even_nums)


def odd(some_numbers: list):
    odd_nums = [digit for digit in some_numbers if int(digit) % 2 == 1]
    return ", ".join(odd_nums)


numbers = input().split(", ")
print(f"Positive: {positive(numbers)}")
print(f"Negative: {negative(numbers)}")
print(f"Even: {even(numbers)}")
print(f"Odd: {odd(numbers)}")