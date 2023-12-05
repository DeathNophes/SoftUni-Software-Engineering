import re

phone_numbers = input()
valid_numbers = []

regex_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex_pattern, phone_numbers)

for match in matches:
    valid_numbers.append(match)
print(', '.join(valid_numbers))

