"""
进程间进行通信 在集群中可能是同一节点 也可能是不同节点
"""
import ray
import os


os.environ['RAY_ACCEL_ENV_VAR_OVERRIDE_ON_ZERO'] = "0"

@ray.remote
def get_value():
    return 42

# 获取远程函数ID 注意ray库在远程函数的时候会直接解析出这个函数的返回值 并不会返回这个函数本身
value_id = get_value.remote()

# 在另一个进程函数中使用该ID
@ray.remote
def use_value(value):
    return value * 2

result = use_value.remote(value_id)

print(ray.get(result))

