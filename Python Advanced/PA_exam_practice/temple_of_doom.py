from collections import deque

tools = deque(int(x) for x in input().split())
substances = [int(x) for x in input().split()]
challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    calculation = tools[0] * substances[-1]

    if calculation in challenges:
        tools.popleft()
        substances.pop()
        challenges.remove(calculation)

    else:
        tools[0] += 1
        tools.rotate(-1)
        substances[-1] -= 1
        if substances[-1] == 0:
            substances.pop()


if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
elif not tools or not substances:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join(str(x) for x in tools)}")
if substances:
    print(f"Substances: {', '.join(str(x) for x in substances)}")
if challenges:
    print(f"Challenges: {', '.join(str(x) for x in challenges)}")