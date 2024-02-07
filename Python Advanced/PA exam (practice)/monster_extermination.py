from collections import deque

monsters_armor = deque(int(x) for x in input().split(','))
soldier_attacks = [int(x) for x in input().split(',')]

killed_monsters = 0

while monsters_armor and soldier_attacks:
    if monsters_armor[0] == soldier_attacks[-1]:
        killed_monsters += 1
        monsters_armor.popleft()
        soldier_attacks.pop()

    elif soldier_attacks[-1] > monsters_armor[0]:
        killed_monsters += 1
        soldier_attacks[-1] -= monsters_armor[0]
        monsters_armor.popleft()
        if len(soldier_attacks) > 1:
            soldier_attacks[-2] += soldier_attacks[-1]
            soldier_attacks.pop()

    elif soldier_attacks[-1] < monsters_armor[0]:
        monsters_armor[0] -= soldier_attacks[-1]
        monsters_armor.rotate(-1)
        soldier_attacks.pop()

if not monsters_armor:
    print("All monsters have been killed!")

if not soldier_attacks:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")

