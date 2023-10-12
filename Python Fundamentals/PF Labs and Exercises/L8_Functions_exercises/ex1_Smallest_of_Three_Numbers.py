def smallest(a, b, c):
    my_list = [a, b, c]
    return min(my_list)


first_num = int(input())
second_num = int(input())
third_num = int(input())

result = smallest(first_num, second_num, third_num)
print(result)
