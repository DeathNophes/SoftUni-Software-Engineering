def data_type():
    data = input()
    input_line = input()

    if data == 'int':
        result = int(input_line) * 2
        return result
    elif data == 'real':
        result = float(input_line) * 1.5
        return f"{result:.2f}"
    elif data == 'string':
        result = f"${input_line}$"
        return result


print(data_type())