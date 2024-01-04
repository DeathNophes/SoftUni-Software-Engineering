from collections import deque

children = deque(input().split())
n = int(input()) - 1

while len(children) != 1:
    count = 0
    while count != n:
        removed = children.popleft()
        children.append(removed)
        count += 1
    print(f"Removed {children.popleft()}")
print(f"Last is {children.popleft()}")