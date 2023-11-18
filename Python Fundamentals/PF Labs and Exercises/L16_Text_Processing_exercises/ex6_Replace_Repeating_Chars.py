some_str = input()
new_str = ''
last_char = ''
for i in range(len(some_str)):
    if some_str[i] != last_char:
        new_str += some_str[i]
        last_char = some_str[i]
print(new_str)
