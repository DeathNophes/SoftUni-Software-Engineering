text = input()
encrypted_text = ''
for symbol in text:
    encrypted_text += chr(ord(symbol) + 3)
print(encrypted_text)