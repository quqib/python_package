"""
更好利用计算机计算资源使用下面两个多线程来弄
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
操作输入输出密集型任务 密集型任务GIL会限制执行速度
import threading
全局解释器锁
global interpreter lock
锁的作用不是控制“启动线程”，而是控制“访问共享数据”
"""
import queue
import random
import threading
import time

from ray.autoscaler.v2.instance_manager.subscribers.threaded_ray_installer import ThreadedRayInstaller


def carwl(link, delay=3):
    # print("现在开始爬取")
    # time.sleep(delay)
    # print("爬取结束，链接为", link)
    pass

links = [
    "http1",
    "http2",
    "http3",
]

# threads = []
#
# for link in links:
#     t = threading.Thread(target=carwl, args=(link,), kwargs={"delay": 2})
#     threads.append(t)
#
# # 启动线程
# for t in threads:
#     t.start()
#
# # 等待线程结束
# for t in threads:
#     t.join()

"""
示例1：
密集型任务 多运算 库使用相关示例
有一个银行账户，初始余额为 1000 元。现在有多个客户（比如 5 个）
同时尝试从该账户中取款。
每次取款金额是随机的（比如 100~300 元之间）。

由于多个线程会同时访问和修改同一个账户余额，
必须使用 线程锁（Lock） 来保证操作的原子性，
防止出现“超支”或数据不一致的问题。
"""
# 原始锁两种状态 锁定（可release） 非锁定（可acquire）这两个方法改变状态后就立即返回

users = [
    'zs',
    'ls',
    'wu',
    'zl',
    'zy',
]

lock = threading.Lock()

manypool = 1000

def getMany(person):
    global manypool
    # 锁应该放在访问共享资源的时候
    print(f"{person}来取钱")
    time.sleep(0.1) # 考虑网络延迟
    # 关键：在操作共享变量时加锁
    with lock:
        amount = random.randint(100, 300)
        if manypool >= amount:
            manypool -= amount
            print(f"{person}取走{amount},余额：{manypool}")

        else:
            print(f"{person}想取{amount}，但余额不足，当前余额：{manypool}")


# threads = []
#
# for user in users:
#     t = threading.Thread(target=getMany, args=(user,))
#     threads.append(t)
#     t.start()
#
#
# # 等待多线程运行完毕
# for t in threads:
#     t.join()



"""
示例2:
    有一个热门商品，初始库存为 10 件。有两类角色：
用户线程（消费者）：共 50 人，每人尝试下单 1 次。下单前需检查库存，若成功则生成订单并扣减库存。
补货线程（生产者）：后台每隔一段时间（如 3 秒）尝试补货 3 件（但总库存不能超过 20）。
所有订单需放入一个线程安全的订单队列，由一个异步发货线程处理（模拟发货）。
如果库存不足，用户进入“候补队列”，最多等待 2 秒，超时则放弃。
系统运行 10 秒后自动关闭所有线程（优雅退出）。
"""
stock = 10
max_stock = 20

# 订单队列
q = queue.Queue()



def user_task(user_id, inventory, order_queue, stop_event):

    pass


def producter():
    global store

    # 判断是否大于20
    if store > max_stock:
        print("仓库获取出现堆积，请抓紧出仓！！！")

    else:
        time.sleep(2)
        store += 3
        print("已经成功进行补货")


threads = []
# 生产者人数
for person in range(1, 51):
    t = threading.Thread(target=user_task, args=(person,),
                         kwargs={
                             "inventory": ""
                         }
                         )
    threads.append(t)









