"""Decorator for measuring run times.

Paramterized version.
"""

import functools
import time
import timeit

run_times = {}


def measure_time(repeat=1):
    """Decorator to measure function run times.
    """
    def _measure_time(func):
        """Function that takes the function that is to be wrapped.
        """
        @functools.wraps(func)
        def _proxy_func(*args, **kwargs):
            """Function that will replace the original function.
            """
            start = timeit.default_timer()
            for _ in range(repeat):
                res = func(*args, **kwargs)
            end = timeit.default_timer()
            key = '.'.join((func.__module__, func.__name__))
            run_times[key] = (end - start) / repeat
            return res
        return _proxy_func
    return _measure_time


# Run the function a hundred time..
@measure_time(100)
def add(arg1, arg2):
    """Test function.
    """
    return arg1 + arg2


# Ones is enough.
@measure_time()
def run_long():
    """Long running function.
    """
    time.sleep(1)


if __name__ == '__main__':
    add(10, 20)
    run_long()
    print(run_times)
