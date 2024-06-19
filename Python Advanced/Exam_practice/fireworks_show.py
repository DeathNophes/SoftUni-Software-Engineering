from collections import deque


def are_we_ready():
    if my_fireworks["Palm Fireworks"] >= 3 and my_fireworks["Willow Fireworks"] >= 3 \
            and my_fireworks["Crossette Fireworks"] >= 3:
        return True
    return False


my_fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0
}

win = False

fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_powers = [int(x) for x in input().split(', ')]

while fireworks_effects and explosive_powers:

    if fireworks_effects[0] <= 0:
        fireworks_effects.popleft()
        continue

    if explosive_powers[-1] <= 0:
        explosive_powers.pop()
        continue

    result = fireworks_effects[0] + explosive_powers[-1]

    if result % 3 == 0 and result % 5 == 0:
        my_fireworks["Crossette Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_powers.pop()

    elif result % 3 == 0:
        my_fireworks["Palm Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_powers.pop()

    elif result % 5 == 0:
        my_fireworks["Willow Fireworks"] += 1
        fireworks_effects.popleft()
        explosive_powers.pop()

    else:
        fireworks_effects[0] -= 1
        fireworks_effects.rotate(-1)

    if are_we_ready():
        win = True
        break

if win:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in fireworks_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

for key, value in my_fireworks.items():
    print(f"{key}: {value}")