import re

pattern = r"[^@:!>-]*@([A-Za-z]+)[^@:!>-]*:([0-9]+)[^@:!>-]*!(A|D)![^@:!>-]*->([0-9]+)[^@:!>-]*"
valid_letters = ['s', 't', 'a', 'r', 'S', 'T', 'A', 'R']
attacked_planets = []
destroyed_planets = []

n = int(input())
for _ in range(n):
    valid_letters_count = 0
    new_line = ""
    line = input()
    for letter in line:
        if letter in valid_letters:
            valid_letters_count += 1
    for char in line:
        new_line += chr(ord(char) - valid_letters_count)
    match = re.fullmatch(pattern, new_line)
    if match:
        if match.group(3) == 'A':
            attacked_planets.append(match.group(1))
        elif match.group(3) == 'D':
            destroyed_planets.append(match.group(1))

sorted_attacked_planets = list(sorted(attacked_planets))
sorted_destroyed_planets = list(sorted(destroyed_planets))

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted_attacked_planets:
    print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted_destroyed_planets:
    print(f"-> {planet}")
