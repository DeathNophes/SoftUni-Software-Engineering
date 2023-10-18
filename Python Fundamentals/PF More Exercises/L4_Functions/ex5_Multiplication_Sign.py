def is_positive(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"

    negative_counter = 0

    if a < 0:
        negative_counter += 1
    if b < 0:
        negative_counter += 1
    if c < 0:
        negative_counter += 1

    if negative_counter % 2 == 0:
        return "positive"
    return "negative"


num1 = int(input())
num2 = int(input())
num3 = int(input())
print(is_positive(num1, num2, num3))
