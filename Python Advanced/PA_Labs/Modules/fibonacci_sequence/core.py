
def create_fibonacci(n):
    sequence = [0, 1]
    first_num = 0
    second_num = 1
    for _ in range(n - 2):
        new_num = first_num + second_num
        first_num = second_num
        second_num = new_num
        sequence.append(new_num)

    return sequence


def locate(number, sequence: list):
    if number in sequence:
        return f"The number - {number} is at index {sequence.index(number)}"
    else:
        return f"The number {number} is not in the sequence"