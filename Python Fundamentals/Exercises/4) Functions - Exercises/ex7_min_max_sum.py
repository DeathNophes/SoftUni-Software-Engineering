def min_max_sum(some_numbers: list):
    numbers_as_int = []
    for number in some_numbers:
        numbers_as_int.append(int(number))
    lowest_num = min(numbers_as_int)
    highest_num = max(numbers_as_int)
    sum_of_numbers = sum(numbers_as_int)
    return lowest_num, highest_num, sum_of_numbers


numbers = input().split()
min_num, max_num, sum_nums = min_max_sum(numbers)
print(f"The minimum number is {min_num}")
print(f"The maximum number is {max_num}")
print(f"The sum number is: {sum_nums}")
