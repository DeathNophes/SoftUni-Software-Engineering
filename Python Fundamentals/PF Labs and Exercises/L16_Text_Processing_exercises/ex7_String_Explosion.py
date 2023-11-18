start_str = input()
final_str = ''
strength = 0
for index in range(len(start_str)):
    if start_str[index] == '>':
        strength += int(start_str[index + 1])
        final_str += '>'
        continue
    if strength > 0:
        strength -= 1
        continue
    final_str += start_str[index]
print(final_str)
