from collections import deque

MAX_CAFFEINE = 300

mg_caffeine = 0

caffeine_sequence = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

while caffeine_sequence and energy_drinks:
    result = caffeine_sequence[-1] * energy_drinks[0]

    if result <= (MAX_CAFFEINE - mg_caffeine):
        mg_caffeine += result
        caffeine_sequence.pop()
        energy_drinks.popleft()

    else:
        caffeine_sequence.pop()
        energy_drinks.rotate(-1)
        mg_caffeine -= 30
        if mg_caffeine < 0:
            mg_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(x) for x in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {mg_caffeine} mg caffeine.")