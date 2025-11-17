import ray
import time
import os

os.environ["RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO"] = "0"

ray.init()

start_time = time.time()

@ray.remote
def square(x):
    time.sleep(0.1)
    return x * x

futures = [square.remote(i) for i in range(4)]
results = ray.get(futures)

end_time = time.time()

print(results, f"第一次消耗时间为{end_time - start_time}")


def ceshi(i):
    time.sleep(0.1)
    return i * i

result = []
for i in range(4):
    result.append(ceshi(i))

end1_time = time.time()

print(result, f"第二次消耗时间为{end1_time - end_time}")



