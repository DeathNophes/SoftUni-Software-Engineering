from collections import deque

BOX_SIZE = 50

boxes_filled = 0

eggs = deque([int(x) for x in input().split(', ')])
papers = [int(x) for x in input().split(', ')]

while eggs and papers:

    if eggs[0] <= 0:
        eggs.popleft()
        continue

    elif eggs[0] == 13:
        eggs.popleft()
        papers[0], papers[-1] = papers[-1], papers[0]
        continue

    result = eggs[0] + papers[-1]

    if result <= BOX_SIZE:
        boxes_filled += 1

    eggs.popleft()
    papers.pop()

if boxes_filled > 0:
    print(f"Great! You filled {boxes_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f"Eggs left: {', '.join(str(x) for x in eggs)}")
elif papers:
    print(f"Pieces of paper left: {', '.join(str(x) for x in papers)}")


