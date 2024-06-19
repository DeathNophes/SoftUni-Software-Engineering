text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
sorted_text = [char for char in text if char.lower() not in vowels]
# Използваме lower(), за да извършим проверката само с малки букви
# case insensitive
print("".join(sorted_text))
