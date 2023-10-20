def version(some_list: list):
    my_list = list(map(int, some_list))
    my_list[-1] += 1
    if my_list[1] == 10:
        my_list[1] = 0
        my_list[0] += 1
    if my_list[2] == 10:
        my_list[2] = 0
        my_list[1] += 1
        if my_list[1] == 10:
            my_list[1] = 0
            my_list[0] += 1
    my_list = list(map(str, my_list))
    return ".".join(my_list)


current_version = input().split(".")
print(version(current_version))
