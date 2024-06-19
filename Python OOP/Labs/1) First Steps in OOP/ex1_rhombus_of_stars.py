def print_upper_rhombus(n):
    for row in range(1, n + 1):
        print(' ' * (n - row) + '* ' * row)


def print_bottom_rhombus(n):
    for row in range(n - 1, -1, -1):
        print(' ' * (n - row) + '* ' * row)


def print_rhombus(n):
    print_upper_rhombus(n)
    print_bottom_rhombus(n)


size = int(input())
print_rhombus(size)