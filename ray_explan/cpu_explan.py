"""
Time: 2026年01月16日10:08:58
Author: Written by Mr.zhaoyang
并发 并行 多进程 多线程 多协程
"""
from multiprocessing import Pool
from multiprocessing import Process
import os


def f(x):
    return x * x

def f_1(name):
    print('hello', name)

# 显示进程ID
def info(title):
    print(title)
    print('mode name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def f_2(name):
    info('function f')
    print('hello', name)


# 这个是最简单的一种调用
# if __name__ == '__main__':
#     # 计算机可以执行上万个进程 一个核在同一时间智能执行一个进程
#     with Pool(5) as p:
#         print(p.map(f, [1, 2, 3]))

# 终结 中断 杀死 进程
# if __name__ == '__main__':
#     p = Process(target=f_1, args=('bob',))
#     p.start()
#     p.join()


if __name__ == '__main__':
    info('main line')
    p = Process(target=f_2, args=('bob',))
    p.start()
    p.join()






