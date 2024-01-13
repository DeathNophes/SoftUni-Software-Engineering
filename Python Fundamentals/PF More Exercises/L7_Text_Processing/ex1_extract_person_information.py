import re

name_pattern = r"@([A-Za-z]+)\|"
age_pattern = r"#(\d+)\*"

n = int(input())
for _ in range(n):
    current_sentence = input()
    name = re.search(name_pattern, current_sentence)
    age = re.search(age_pattern, current_sentence)
    print(f"{name.group(1)} is {age.group(1)} years old.")