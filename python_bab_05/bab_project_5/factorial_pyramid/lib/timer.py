"""
    This Module times a peice of function/ class method
"""

import time


def time_it(func):
    def _(*args, **kwargs):
        start_time = time.time()
        val = func(*args, **kwargs)   # add(x, y)
        end_time = time.time()
        time_elapsed = end_time - start_time
        print(f"Time Elapsed: {time_elapsed}")
        return val
    return _