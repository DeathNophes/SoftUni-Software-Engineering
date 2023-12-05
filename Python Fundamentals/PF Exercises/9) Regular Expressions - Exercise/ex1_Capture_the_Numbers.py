import re

line = input()
pattern = r"\d+"

while line:     # While we have an input
    matches = re.findall(pattern, line)     # It creates a list with the matches
    if matches:     # If there are any matches
        print(' '.join(matches), end=' ')
    line = input()
