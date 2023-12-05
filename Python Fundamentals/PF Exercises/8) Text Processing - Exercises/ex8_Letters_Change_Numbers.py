from string import ascii_lowercase
sequence = input().split()
total_value = 0
for curr_string in sequence:
    curr_value = 0
    first_letter = curr_string[0]
    last_letter = curr_string[-1]
    number = int(curr_string[1:-1])
    index_first = ascii_lowercase.index(first_letter.lower()) + 1
    index_last = ascii_lowercase.index(last_letter.lower()) + 1
    if first_letter.isupper():
        curr_value += (number / index_first)
    else:
        curr_value += (number * index_first)

    if last_letter.isupper():
        curr_value -= index_last
    else:
        curr_value += index_last

    total_value += curr_value
print(f"{total_value:.2f}")
