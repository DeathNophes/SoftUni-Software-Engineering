def is_perfect(some_number):
    divisors_sum = 0
    for divisor in range(1, some_number):
        if some_number % divisor == 0:
            divisors_sum += divisor
    if some_number == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."
    # Търсим число, което е равно на сумата на всичките си точни делители


number = int(input())
print(is_perfect(number))