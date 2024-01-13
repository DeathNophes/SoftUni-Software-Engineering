word = input()
words_list = []

for i in range(len(word)):
    if word[i].isupper():
        words_list += [i]

print(words_list)
