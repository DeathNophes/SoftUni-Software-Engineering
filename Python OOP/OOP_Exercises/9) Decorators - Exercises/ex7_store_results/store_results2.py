def store_results(func):
    _FILE_PATH = 'results.txt'

    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        with open(_FILE_PATH, 'a') as results_file:
            results_file.write(
                f"Function '{func.__name__}' was called. Result: {result}\n"
            )

    return wrapper