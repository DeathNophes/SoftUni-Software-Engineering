numbers_as_str = input().split()
numbers_as_int = []
for number in numbers_as_str:
    numbers_as_int.append(int(number))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_int))
print(result)
