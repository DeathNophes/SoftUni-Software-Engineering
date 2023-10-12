def is_palindrome(some_number: str):
    if some_number == some_number[::-1]:
        return True
    return False


numbers_as_str = input().split(", ")
for number in numbers_as_str:
    print(is_palindrome(number))
