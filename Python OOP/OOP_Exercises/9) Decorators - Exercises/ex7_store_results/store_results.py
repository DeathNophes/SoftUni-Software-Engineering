class store_results:
    FILE_PATH = 'results.txt'

    def __init__(self, func):   # Our decorator
        self.func = func

    def __call__(self, *args, **kwargs):    # The same as wrapper
        result = self.func(*args, **kwargs)

        with open(store_results.FILE_PATH, 'a') as file:
            file.write(
                f"Function '{self.func.__name__}' was called. Result: {result}\n"
            )
