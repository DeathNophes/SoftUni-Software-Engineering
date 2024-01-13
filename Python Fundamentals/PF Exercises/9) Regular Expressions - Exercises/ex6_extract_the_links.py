import re

sentence = input()
pattern = r'w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+'

while sentence:
    valid_link = re.search(pattern, sentence)
    if valid_link:
        print(valid_link.group())
    sentence = input()
