def odd_even(digits: str):
    even_sum = 0
    odd_sum = 0
    for digit in digits:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    return even_sum, odd_sum


numbers = input()
sum_even_digits, sum_odd_digits = odd_even(numbers)
print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")
