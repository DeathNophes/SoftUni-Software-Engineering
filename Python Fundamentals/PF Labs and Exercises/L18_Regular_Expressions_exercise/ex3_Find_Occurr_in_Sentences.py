import re

sentence = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'

result = re.findall(pattern, sentence, re.IGNORECASE)
print(len(result))
