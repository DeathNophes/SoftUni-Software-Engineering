sequence = [int(digit) for digit in input().split()]
total_value = 0
while sequence:
    given_index = int(input())

    if given_index < 0:
        number = sequence[0]
        sequence[0], sequence[-1] = sequence[-1], sequence[-1]
    elif given_index > len(sequence) - 1:
        number = sequence[-1]
        sequence[0], sequence[-1] = sequence[0], sequence[0]
    else:
        number = sequence.pop(given_index)

    total_value += number

    for index, current_number in enumerate(sequence):
        if current_number <= number:
            sequence[index] += number
        else:
            sequence[index] -= number

print(total_value)
