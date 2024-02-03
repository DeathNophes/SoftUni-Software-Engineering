import os

symbols = ("-", ",", ".", "!", "?")
path = os.path.join("files", "file_1.txt")

with open(path, 'r') as even_lines_file:
    text = even_lines_file.readlines()
    # We make this a list of strings

for row in range(0, len(text), 2):
    # We want only the even rows
    for symbol in symbols:
        text[row] = text[row].replace(symbol, '@')

    print(*text[row].split()[::-1])
    # We unpack the row (list) reversed
