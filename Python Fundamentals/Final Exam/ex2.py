import re

n = int(input())
pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#'
for _ in range(n):
    person = input()
    match = re.search(pattern, person)
    if match:
        print(f"{match.group(1)}, The {match.group(2)}")
        print(f">> Strength: {len(match.group(1))}")
        print(f">> Armor: {len(match.group(2))}")
    else:
        print('Access denied!')