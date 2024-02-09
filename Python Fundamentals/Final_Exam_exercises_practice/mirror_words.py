import re

string = input()
pattern = r'(@|#)([A-Za-z]{3,})(\1{2})([A-Za-z]{3,})\1'
valid_pairs = []

matches = re.findall(pattern, string)
pairs_count = len(matches)

for match in matches:
    if match[1] == match[3][::-1]:
        valid_pairs.append(f'{match[1]} <=> {match[3]}')

if pairs_count > 0:
    print(f"{pairs_count} word pairs found!")
else:
    print('No word pairs found!')
if valid_pairs:
    print('The mirror words are:')
    print(', '.join(valid_pairs))
else:
    print('No mirror words!')