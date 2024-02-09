def func_executor(*func_data):
    result = []

    for func, args in func_data:
        result.append(f"{func.__name__} - {func(*args)}") # We unpack them here

    return "\n".join(result)
