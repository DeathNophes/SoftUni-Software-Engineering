from collections import deque

quantity = int(input())
orders = deque(int(x) for x in input().split())

print(max(orders))
while orders:
    current_order = int(orders.popleft())
    quantity -= current_order
    if quantity >= 0:
        continue
    else:
        print(f"Orders left: {current_order}", end=' ')
        while orders:
            print(orders.popleft(), end=' ')
        break

if quantity >= 0:
    print("Orders complete")