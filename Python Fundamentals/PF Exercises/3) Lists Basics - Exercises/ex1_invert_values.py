my_list = input().split()
invert_list = []
for i in my_list:
    current_num = -int(i)
    invert_list.append(current_num)
print(invert_list)