from string import punctuation

text = input()
digits = [symbol for symbol in text if symbol.isdigit()]
letters = [symbol for symbol in text if symbol.isalpha()]
others = [symbol for symbol in text if symbol in punctuation]

print(''.join(digits))
print(''.join(letters))
print(''.join(others))
