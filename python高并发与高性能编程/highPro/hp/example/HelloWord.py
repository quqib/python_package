"""
Time: 2026年03月10日 11:56:40
Author: Written by Mr.zhaoyang
"""
from threading import Thread

"""

"""
# 类和对象
class HelloPython:
    strA = 'strA'
    strB = 'strB'
    numsA = 6
    numsB = 6

    def hello(self):
        print(f"Hello, {self.strA} and {self.strB}!")

    def word(self):
        print(f"Word, {self.strA} and {self.strB}!")



# 进程和线程
"""
python线程⑦个状态：
    线程创建状态
    线程就绪状态
    线程运行状态
    线程终止状态
    线程等待状态
    线程阻塞状态
    线程结束状态
Cpython虚拟机中，多线程是通过切换线程上下文进行熟悉爱你的，线程切换会造成资源开销
    线程锁用来保护线程的安全
    
"""

import threading
import time

# 存在GIL时的线程开销
def readFile():
    print("线程:" + str(threading.current_thread().name) + "开始执行...")
    start = time.time()
    with open("file.txt", "r") as f:
        data = f.read()
        print(data)
    end = time.time()
    print(f"线程:{threading.current_thread().name}执行完成，耗时:{end - start:.2f}秒")


t1 = Thread(target=readFile)
t2 = Thread(target=readFile)

t1.start()
t2.start()
