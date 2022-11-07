import asyncio

# concurrent.future.Future对象主要用于线程池和进程池异步操作时的对象
import time

from concurrent.futures import Future
from concurrent.futures.thread import ThreadPoolExecutor  # 线程池
from concurrent.futures.process import ProcessPoolExecutor  # 进程池


def func(value):
    time.sleep(2)
    # print(value)
    return "22"


# 创建线程,并规定最大线程数
pool = ThreadPoolExecutor(5)

for i in range(10):
    fut = pool.submit(func, i)
    print(fut.result())
    print(fut)

