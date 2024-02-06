from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

all_worms_have_holes = True
matches = 0
while worms and holes:
    if worms[-1] == holes[0]:
        worms.pop()
        matches += 1

    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            all_worms_have_holes = False
            worms.pop()

    holes.popleft()

if matches:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and all_worms_have_holes:
    print("Every worm found a suitable hole!")
elif not worms and not all_worms_have_holes:
    print("Worms left: none")
else:
    print(f"Worms left: {', '.join(str(worm) for worm in worms)}")

if not holes:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join(str(hole) for hole in holes)}")
