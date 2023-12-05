import re

text = input()
cool_threshold = 1

pattern_emojis = r'(::|\*\*)([A-Z][a-z]{2,})\1'
pattern_digits = r'\d'

valid_emojis = re.finditer(pattern_emojis, text)
digits = re.findall(pattern_digits, text)
valid_emojis2 = re.findall(pattern_emojis, text)
cool_emojis = []

for digit in digits:
    cool_threshold *= int(digit)

for emoji in valid_emojis:
    if '::' in emoji.group():
        curr_emo = emoji.group().replace('::', '')
        coolness = 0
        for symbol in curr_emo:
            coolness += ord(symbol)
        if coolness >= cool_threshold:
            cool_emojis.append(emoji.group())

    else:
        curr_emo = emoji.group().replace('**', '')
        coolness = 0
        for symbol in curr_emo:
            coolness += ord(symbol)
        if coolness >= cool_threshold:
            cool_emojis.append(emoji.group())

print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis2)} emojis found in the text. The cool ones are:")
for curr_emoji in cool_emojis:
    print(curr_emoji)