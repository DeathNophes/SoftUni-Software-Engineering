import re

name_pattern = r"[a-zA-Z]"
km_pattern = r"\d"

players = {}
available_names = input().split(', ')

text = input()
while text != "end of race":
    name = "".join(re.findall(name_pattern, text))
    distance = sum([int(x) for x in re.findall(km_pattern, text)])

    if name not in players.keys() and name in available_names:
        players[name] = distance
    elif name in players.keys():
        players[name] += distance

    text = input()

sorted_players = dict(sorted(players.items(), key=lambda x: x[1], reverse=True))

i = 1
for curr_name in sorted_players.keys():
    if i == 1:
        print(f"{i}st place: {curr_name}")
    elif i == 2:
        print(f"{i}nd place: {curr_name}")
    elif i == 3:
        print(f"{i}rd place: {curr_name}")
    i += 1
    if i == 4:
        break
