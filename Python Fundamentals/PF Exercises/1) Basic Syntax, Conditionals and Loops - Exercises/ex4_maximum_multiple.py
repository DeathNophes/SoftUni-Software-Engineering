divisor = int(input())
boundary = int(input())

for number in range(boundary, divisor - 1, -1):
    if number % divisor == 0:
        print(number)
        break

    # Това е просто интелигентен начин да се напише тази програма!