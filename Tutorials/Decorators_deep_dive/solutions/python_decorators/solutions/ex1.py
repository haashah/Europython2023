"""Decorator for measuring run times.
"""

import functools
import time
import timeit

run_times = {}


def measure_time(func):
    """Decorator to measure function run times.
    """
    @functools.wraps(func)
    def _proxy_func(*args, **kwargs):
        """Function that will replace the original function.
        """
        start = timeit.default_timer()
        res = func(*args, **kwargs)
        end = timeit.default_timer()
        key = '.'.join((func.__module__, func.__name__))
        run_times[key] = end - start
        return res
    return _proxy_func


@measure_time
def add(arg1, arg2):
    """Test function.
    """
    return arg1 + arg2


@measure_time
def run_long():
    """Long running function.
    """
    time.sleep(1)


if __name__ == '__main__':
    add(10, 20)
    run_long()
    print(run_times)
