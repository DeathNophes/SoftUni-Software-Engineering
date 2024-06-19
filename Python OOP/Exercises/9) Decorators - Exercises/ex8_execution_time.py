from time import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time()              # Get the current time
        func(*args, **kwargs)
        return time() - start       # Current time - start time

    return wrapper
