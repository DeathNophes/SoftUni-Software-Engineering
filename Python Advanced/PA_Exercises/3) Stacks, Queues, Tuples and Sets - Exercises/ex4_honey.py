from collections import deque

bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
symbols = deque(char for char in input().split())
honey = 0

while bees and nectar:
    if bees[0] > nectar[-1]:
        nectar.pop()
        continue
    else:
        operator = symbols.popleft()
        if operator == '+':
            honey += abs(bees[0] + nectar[-1])
        elif operator == '-':
            honey += abs(bees[0] - nectar[-1])
        elif operator == '*':
            honey += abs(bees[0] * nectar[-1])
        elif operator == '/':
            if nectar[-1] == 0:
                bees.popleft()
                nectar.pop()
                continue
            honey += abs(bees[0] / nectar[-1])
        bees.popleft()
        nectar.pop()

print(f"Total honey made: {honey}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")