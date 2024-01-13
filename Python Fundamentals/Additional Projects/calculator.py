def addition(a, b: int):
    result = a + b
    return result


def subtraction(a, b: int):
    result = a - b
    return result


def multiplication(a, b: int):
    result = a * b
    return result


def division(a, b: int):
    if a == 0 or b == 0:
        return "Error"
    result = a / b
    return result


def main():
    main_data = int(input("Menu:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Quit\n\n"
                          "Enter your choice(1/2/3/4/5): "))
    if main_data == 5:
        return "Quit"
    first_num = int(input("Enter the first number: "))
    second_num = int(input("Enter the second number: "))
    if main_data == 1:
        return addition(first_num, second_num)
    elif main_data == 2:
        return subtraction(first_num, second_num)
    elif main_data == 3:
        return multiplication(first_num, second_num)
    elif main_data == 4:
        return division(first_num, second_num)


while True:
    data = main()
    if data == 'Quit':
        print("Goodbye")
        break
    print(f"The final result is: {data}")
