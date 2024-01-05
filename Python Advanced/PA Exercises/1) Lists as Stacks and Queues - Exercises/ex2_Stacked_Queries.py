stack = []
n = int(input())

for _ in range(n):
    query = input().split()
    if '1' in query:
        number = int(query[1])
        stack.append(number)
    elif len(stack) != 0:   # We check if there are elements in the stack
        if '2' in query:
            stack.pop()
        elif '3' in query:
            print(max(stack))
        elif '4' in query:
            print(min(stack))

while stack:
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop(), end=', ')
