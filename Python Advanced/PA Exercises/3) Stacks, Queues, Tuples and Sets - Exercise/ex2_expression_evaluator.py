from collections import deque

numbers = deque()
expression = input().split()

for char in expression:
    if char not in '+-*/':  # The valid operators
        numbers.append(int(char))
    else:
        while len(numbers) > 1:     # We will need the last number in there
            first_num = numbers.popleft()
            second_num = numbers.popleft()
            if char == '+':
                numbers.appendleft(first_num + second_num)
            elif char == '-':
                numbers.appendleft(first_num - second_num)
            elif char == '*':
                numbers.appendleft(first_num * second_num)
            elif char == '/':
                numbers.appendleft(first_num // second_num)

print(numbers.popleft())
