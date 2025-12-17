import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        print(f"函数{func.__name__}执行耗时：{elapsed_time:.6f}")
        print(result)
        return result
    return wrapper


@timer
def test():
    i = 0
    for i in range(1, 10000):
        for j in range(1, 1000):
            i += 1

    return i

test()


