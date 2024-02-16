from collections import deque

vowels = deque(input().split())
consonants = input().split()

found_word = ""
word_found_flag = False

my_words = {
    "rose": ['r', 'o', 's', 'e'],
    "tulip": ['t', 'u', 'l', 'i', 'p'],
    "lotus": ['l', 'o', 't', 'u', 's'],
    "daffodil": ['d', 'a', 'f', 'o', 'i', 'l']
}

while vowels and consonants:
    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for word in my_words.keys():
        if first_vowel in my_words[word]:
            my_words[word].remove(first_vowel)
        if last_consonant in my_words[word]:
            my_words[word].remove(last_consonant)
        if len(my_words[word]) == 0:
            found_word = word
            word_found_flag = True
            break

    if word_found_flag:
        break

if word_found_flag:
    print(f"Word found: {found_word}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")