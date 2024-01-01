import re

demons_dict = {}
digits_pattern = r"[+-]?[0-9.]+"
letters_pattern = r"[^0-9+*/.-]"
symbols_pattern = r"\*|\/"

demons = [demon.replace(" ", "") for demon in input().split(',')]

for demon in demons:
    digits = re.findall(digits_pattern, demon)
    letters = re.findall(letters_pattern, demon)
    symbols = re.findall(symbols_pattern, demon)
    damage = sum([float(digit) for digit in digits])
    health = sum([ord(x) for x in letters])
    for symbol in symbols:
        if symbol == '*':
            damage *= 2
        elif symbol == '/':
            damage /= 2
    demons_dict[demon] = {'health': health, 'damage': damage}


for curr_demon in sorted(demons_dict.keys()):
    curr_health = demons_dict[curr_demon]['health']
    curr_damage = demons_dict[curr_demon]['damage']
    print(f"{curr_demon} - {curr_health} health, {curr_damage:.2f} damage")
