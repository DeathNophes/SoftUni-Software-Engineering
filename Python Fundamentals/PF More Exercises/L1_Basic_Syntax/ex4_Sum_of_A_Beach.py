word = input()
words_list = ['Sand', 'Water', 'Fish', 'Sun']
word_counter = 0

for i in words_list:
    if i.lower() in word.lower():
        word_counter += word.lower().count(i.lower())
print(word_counter)
