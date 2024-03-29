from collections import deque

elves_energy = deque([int(x) for x in input().split()])
materials = [int(x) for x in input().split()]

toys = 0
total_energy = 0

count = 0

while elves_energy and materials:

    if elves_energy[0] < 5:
        elves_energy.popleft()
        continue

    count += 1

    if count % 3 == 0 and count % 5 == 0:
        if elves_energy[0] >= (materials[-1] * 2):
            elves_energy[0] -= (materials[-1] * 2)
            total_energy += (materials[-1] * 2)
            elves_energy.rotate(-1)
            materials.pop()
        else:
            elves_energy[0] *= 2
            elves_energy.rotate(-1)

    elif count % 3 == 0:
        if elves_energy[0] >= (materials[-1] * 2):
            toys += 2
            elves_energy[0] -= (materials[-1] * 2)
            total_energy += (materials[-1] * 2)
            elves_energy[0] += 1
            elves_energy.rotate(-1)
            materials.pop()
        else:
            elves_energy[0] *= 2
            elves_energy.rotate(-1)

    elif count % 5 == 0:
        if elves_energy[0] >= materials[-1]:
            elves_energy[0] -= materials[-1]
            total_energy += materials[-1]
            elves_energy.rotate(-1)
            materials.pop()
        else:
            elves_energy[0] *= 2
            elves_energy.rotate(-1)

    else:
        if elves_energy[0] >= materials[-1]:    # If the elf has enough energy
            toys += 1                           # A toy is created
            elves_energy[0] -= materials[-1]    # We remove the energy from the elf
            total_energy += materials[-1]       # We add to the total energy
            elves_energy[0] += 1                # The elf ate a cookie
            elves_energy.rotate(-1)             # The elf got to the back of the line
            materials.pop()                     # We remove the box with materials

        else:
            elves_energy[0] *= 2                # The elf drinks hot chocolate
            elves_energy.rotate(-1)             # The elf got to the back of the line

print(f"Toys: {toys}")
print(f"Energy: {total_energy}")

if elves_energy:
    print(f"Elves left: {', '.join(str(x) for x in elves_energy)}")
if materials:
    print(f"Boxes left: {', '.join(str(x) for x in materials)}")