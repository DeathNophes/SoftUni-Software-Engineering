from collections import deque

cups = deque(int(x) for x in input().split())
bottles = deque(int(y) for y in input().split())

wasted_water = 0
no_more_bottles = False
all_cups_are_full = False

while True:
    if not cups:
        all_cups_are_full = True
        break
    if not bottles:
        no_more_bottles = True
        break

    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle == current_cup:
        continue
    elif current_bottle > current_cup:
        wasted_water += (current_bottle - current_cup)
    elif current_bottle < current_cup:
        diff = current_cup - current_bottle
        cups.insert(0, diff)

if all_cups_are_full:
    bottles_as_str = [str(bottle) for bottle in bottles]
    print(f"Bottles: {' '.join(bottles_as_str)}")
    print(f"Wasted litters of water: {wasted_water}")

if no_more_bottles:
    cups_as_str = [str(cup) for cup in cups]
    print(f"Cups: {' '.join(cups_as_str)}")
    print(f"Wasted litters of water: {wasted_water}")