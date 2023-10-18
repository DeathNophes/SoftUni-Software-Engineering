from math import floor


def distance(_x1, _y1, _x2, _y2):
    return abs(_x2 - _x1) + abs(_y2 - _y1)


x1 = floor(float(input()))
y1 = floor(float(input()))
x2 = floor(float(input()))
y2 = floor(float(input()))
x3 = floor(float(input()))
y3 = floor(float(input()))
x4 = floor(float(input()))
y4 = floor(float(input()))

coordinates1 = distance(x1, y1, 0, 0)
coordinates2 = distance(x2, y2, 0, 0)
coordinates3 = distance(x3, y3, 0, 0)
coordinates4 = distance(x4, y4, 0, 0)

line_1 = coordinates1 + coordinates2
line_2 = coordinates3 + coordinates4

if line_1 >= line_2:
    if coordinates1 <= coordinates2:
        print(f'({x1}, {y1})({x2}, {y2})')
    else:
        print(f'({x2}, {y2})({x1}, {y1})')
if line_1 < line_2:
    if coordinates3 <= coordinates4:
        print(f'({x3}, {y3})({x4}, {y4})')
    else:
        print(f'({x4}, {y4})({x3}, {y3})')
