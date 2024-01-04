from collections import deque

customer_deque = deque()
name = input()

while name != 'End':
    if name == 'Paid':
        while customer_deque:
            print(customer_deque.popleft())
    else:
        customer_deque.append(name)
    name = input()

print(f"{len(customer_deque)} people remaining.")