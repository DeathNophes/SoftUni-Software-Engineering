import os
from string import punctuation

path = os.path.join("files", "file_1.txt")
output_file_path = os.path.join("files", "output_2.txt")

with open(path, 'r') as text_file:
    text = text_file.readlines()

output_file = open(output_file_path, 'w')
for row in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[row]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {row + 1}: {''.join(text[row][:-1])} ({letters})({marks})\n")

output_file.close()
# When we are not using the 'with' statement we need to close our file with close()
