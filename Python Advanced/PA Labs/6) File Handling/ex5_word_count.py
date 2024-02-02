import os
import re

words_path = os.path.join("resources", "words.txt")
text_path = os.path.join("resources", "input_file.txt")
output_file = os.path.join("resources", "output.txt")

with open(words_path) as file:
    searched_words = file.read()
    searched_words_list = [word.lower() for word in searched_words.split()]

with open(text_path) as file:
    content = file.read().lower()

words_count = {}

for word in searched_words_list:
    pattern = rf"\b{word}\b"
    results = re.findall(pattern, content)
    words_count[word] = results.count(word)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output_file, 'w') as file:
    for word, count in sorted_words_count:
        file.write(f"{word} - {count}\n")
