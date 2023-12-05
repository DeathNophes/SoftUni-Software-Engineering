def characters(first, second):
    for i in range(ord(first) + 1, ord(second)):
        print(chr(i), end=" ")


first_char = input()
second_char = input()
characters(first_char, second_char)
