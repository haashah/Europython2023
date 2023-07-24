import functools
from timeit import default_timer



def measure_runtime(func):
    times = []

    @functools.wraps(func)
    def _runtime(*args, **kwargs):
        n = 1000
        start_time = default_timer()
        for _ in range(n):
            res = func(*args, **kwargs)
        run_time = default_timer() - start_time / n
        times.append(run_time)
        print("runtime:", run_time)
        return res
    _runtime.times = times
    return _runtime


TIME_MEASUREMENT_ON = True

def measure_runtime_parameterized(n):
    num_execs = n
    @functools.wraps(_runtime)
    def _runtime(func):
        times = []
        @functools.wraps(__runtime)
        def __runtime(*args, **kwargs):
            start_time = default_timer()
            for _ in range(num_execs):
                res = func(*args, **kwargs)
            if TIME_MEASUREMENT_ON:
                run_time = default_timer() - start_time / num_execs
                times.append(run_time)
                print("runtime:", run_time)
            return res
        return __runtime
    return _runtime

    





