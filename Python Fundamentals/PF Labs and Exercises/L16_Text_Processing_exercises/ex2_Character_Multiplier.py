def which_is_bigger(_str1, _str2):
    if len(_str1) >= len(_str2):
        return _str1, _str2
    return _str2, _str1


output = 0
str1, str2 = input().split()
bigger_str, smaller_str = which_is_bigger(str1, str2)


for i in range(len(bigger_str)):
    if i < len(smaller_str):
        output += (ord(bigger_str[i]) * ord(smaller_str[i]))
    else:
        output += ord(bigger_str[i])

print(output)