expression = input()
stack = []
for index in range(len(expression)):
    if expression[index] == '(':
        stack.append(index)
    elif expression[index] == ')':
        start = stack.pop()
        print(expression[start:index + 1])
