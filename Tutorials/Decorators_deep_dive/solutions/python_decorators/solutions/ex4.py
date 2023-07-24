"""Decorator for measuring run times.

Turn measurement on/off.
"""

import functools
import time
import timeit

MEASURE = True
RUN_TIMES = {}


def measure_time(repeat=1, run_times=None):
    """Decorator to measure function run times.
    """
    if run_times is None:
        run_times = RUN_TIMES

    def _measure_time(func):
        """Function that takes the function that is to be wrapped.
        """
        if MEASURE:
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
        return func
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
    print('RUN_TIMES:', RUN_TIMES)
