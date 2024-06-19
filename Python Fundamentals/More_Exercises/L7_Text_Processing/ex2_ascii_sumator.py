first_char = input()
second_char = input()
text = input()

chars_list = []
total_value = 0

first_char_ascii = ord(first_char)
second_char_ascii = ord(second_char)

for i in range(first_char_ascii + 1, second_char_ascii):
    chars_list.append(chr(i))

for j in text:
    if j in chars_list:
        total_value += ord(j)

print(total_value)

