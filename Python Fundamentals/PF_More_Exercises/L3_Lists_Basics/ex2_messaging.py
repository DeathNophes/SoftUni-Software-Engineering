numbers = input().split()
given_string = list(input())
my_text = []
for i in range(len(numbers)):
    sum_of_numbers = 0
    for j in numbers[i]:
        sum_of_numbers += int(j)
    while sum_of_numbers >= len(given_string):
        sum_of_numbers -= len(given_string)
    my_text.append(given_string[sum_of_numbers])
    given_string.pop(sum_of_numbers)
print("".join(my_text))
