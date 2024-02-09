from math import floor, sqrt


def closest_to_center(x1, y1, x2, y2):
    c1 = sqrt(x1 * x1 + y1 * y1)
    c2 = sqrt(x2 * x2 + y2 * y2)

    if c1 > c2:
        x, y = x2, y2
    elif c1 <= c2:
        x, y = x1, y1

    return f"({x}, {y})"


num1 = floor(float(input()))
num2 = floor(float(input()))
num3 = floor(float(input()))
num4 = floor(float(input()))
print(closest_to_center(num1, num2, num3, num4))
