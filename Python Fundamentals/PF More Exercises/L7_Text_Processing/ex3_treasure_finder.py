import re

key = [int(x) for x in input().split()]

text = input()
while text != "find":
    i = 0
    new_text = ""
    while i != len(text):
        if i >= len(key):
            j = i % len(key)
            new_text += chr(ord(text[i]) - key[j])
        else:
            new_text += chr(ord(text[i]) - key[i])
        i += 1

    pattern = r"&([A-Za-z]+)&|<(.+)>"
    treasure_info = re.findall(pattern, new_text)
    treasure = treasure_info[0][0]
    coordinates = treasure_info[1][1]
    print(f"Found {treasure} at {coordinates}")

    text = input()
