from string import ascii_letters, punctuation, whitespace


initial_string = input()
numbers_list = [num for num in initial_string if num.isdigit()]
non_numbers_list = [symbol for symbol in initial_string
                    if symbol in ascii_letters or symbol in punctuation or symbol in whitespace]
take_list = []
skip_list = []

result = ""

for i in range(len(numbers_list)):
    if i % 2 == 0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])

for index in range(len(take_list)):
    m = int(take_list[index])
    n = int(skip_list[index])

    if m >= 0 and non_numbers_list:
        if m >= len(non_numbers_list):
            m = len(non_numbers_list)
        for i in range(0, m):
            taken_symbol = non_numbers_list[i]
            result += taken_symbol
        del non_numbers_list[0: m]

    if n > 0 and non_numbers_list:
        n -= 1
        while n >= 0:
            non_numbers_list.pop(n)
            n -= 1

print(result)
