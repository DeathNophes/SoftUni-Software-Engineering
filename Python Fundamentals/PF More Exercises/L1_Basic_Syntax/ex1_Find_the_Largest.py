def largest(some_numbers: str) -> list:
    int_list = []
    my_list = []
    for i in range(len(some_numbers)):
        int_list.append(int(some_numbers[i]))
    for num in range(len(int_list)):
        my_list.append(max(int_list))
        int_list.remove(max(int_list))
    return my_list


number = input()
result = largest(number)
for i in range(len(result)):
    print(result[i], end="")

