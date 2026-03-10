"""
ray是分布式并行计算框架
多线程 多进程 并行库
线程：threading
进程：multiprocessing
"""

import ray
import time
import os

# 斐波那契额数列 f(n) + f(n+1) = f(n+2)

a = [1, 2, 3, 4, 5]


# print(round((a[len(a)//2] + a[len(a)//2 - 1])/2, 5))

for i in range(1, 10):
    for j in range(1, i + 1):
        # 格式化占2位，保证对齐
        # print(f'{j}×{i}={i*j:2d}', end='\t')
        pass
    # 一行结束换行
    # print()


a = '123'
print(a.startswith(""))


