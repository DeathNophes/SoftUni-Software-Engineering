def get_factorial(n):
    if n == 0:
        return 1

    return n * get_factorial(n - 1)


num = int(input())
print(get_factorial(num))