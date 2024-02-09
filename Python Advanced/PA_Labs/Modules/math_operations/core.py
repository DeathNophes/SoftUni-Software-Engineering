def add(num1, num2):
    return f"{(num1 + num2):.2f}"


def subtract(num1, num2):
    return f"{(num1 - num2):.2f}"


def divide(num1, num2):
    try:
        return f"{(num1 / num2):.2f}"
    except ZeroDivisionError:
        return "We can't divide by zero"


def multiply(num1, num2):
    return f"{(num1 * num2):.2f}"


def power(num1, num2):
    return f"{(num1 ** num2):.2f}"


sign_mapper = {
    '+': add,
    '-': subtract,
    '/': divide,
    '*': multiply,
    '^': power
}


def execute_expression(exp):
    num1_text, sign, num2_text = exp.split()
    num1 = float(num1_text)
    num2 = float(num2_text)

    return sign_mapper[sign](num1, num2)

