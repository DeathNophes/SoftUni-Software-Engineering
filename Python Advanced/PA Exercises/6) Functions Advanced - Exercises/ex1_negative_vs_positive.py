def print_numbers(numbers: list) -> None:
    positive_sum = sum(num for num in numbers if num > 0)
    negative_sum = sum(num for num in numbers if num < 0)

    print(negative_sum)
    print(positive_sum)

    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


nums = [int(x) for x in input().split()]
print_numbers(nums)
