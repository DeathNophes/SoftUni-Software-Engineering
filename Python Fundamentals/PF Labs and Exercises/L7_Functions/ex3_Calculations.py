def calculation(a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b
    else:
        return "Wrong operator!"


operator = input("Choose your action(+ - * /): ")
first_num = int(input("Enter the first number: "))
second_num = int(input("Enter the second number: "))
result = calculation(first_num, second_num)
print(result)
