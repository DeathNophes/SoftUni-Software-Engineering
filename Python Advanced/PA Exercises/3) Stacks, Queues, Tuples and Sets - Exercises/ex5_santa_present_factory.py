from collections import deque

materials = [int(x) for x in input().split()]
magic = deque(int(x) for x in input().split())

points = {150: 'Doll', 250: 'Wooden train', 300: 'Teddy bear', 400: 'Bicycle'}
presents = {}

while materials and magic:
    if materials[-1] == 0 and magic[0] == 0:
        materials.pop()
        magic.popleft()
        continue
    elif materials[-1] == 0:
        materials.pop()
        continue
    elif magic[0] == 0:
        magic.popleft()
        continue

    result = materials[-1] * magic[0]
    if result in points.keys():
        new_present = points[result]    # We get the name of the new present
        if new_present not in presents:
            presents[new_present] = 0
        presents[new_present] += 1      # We add one to the present
        materials.pop()
        magic.popleft()
    elif result < 0:
        materials.append(materials.pop() + magic.popleft())
    elif result > 0:
        magic.popleft()
        materials[-1] += 15

if ('Doll' in presents and 'Wooden train' in presents) or ('Teddy bear' in presents and 'Bicycle' in presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials[::-1]])}")
if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

for key, value in sorted(presents.items()):
    print(f"{key}: {value}")