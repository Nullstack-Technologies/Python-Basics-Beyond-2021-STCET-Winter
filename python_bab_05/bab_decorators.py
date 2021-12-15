"""
    Decorators
"""
import time


def timer(func):
    def _(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)   # add(x, y)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"Time Elapsed: {time_elapsed}")
        return val
    return _


@timer
def add(x, y):
    return x + y

add(1, 2)