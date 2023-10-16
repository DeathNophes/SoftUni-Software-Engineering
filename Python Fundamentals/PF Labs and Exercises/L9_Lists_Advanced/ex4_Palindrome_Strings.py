def is_palindrome(word):
    if word[::-1] == word:
        return word


strings = input().split()
searched_palindrome = input()

palindromes_list = [word for word in strings if is_palindrome(word)]
palindrome_counter = palindromes_list.count(searched_palindrome)

print(palindromes_list)
print(f"Found palindrome {palindrome_counter} times")
