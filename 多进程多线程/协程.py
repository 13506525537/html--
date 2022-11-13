import asyncio


# 示例1
async def func1():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return "任务完成1"


async def func2():
    print(3)
    await asyncio.sleep(1)
    print(4)
    return "任务完成2"


async def main():
    print(3)
    response1 = asyncio.create_task(func1())
    print(response1)

    response2 = asyncio.create_task(func1())
    print(response2)
    res1 = await response1
    res2 = await response2
    print(res1, res2)
    print(4)


# asyncio.run(main())
# print("qita")

# 示例2

async def main2():
    print("任务开始")
    task_list = [asyncio.create_task(func1(), name="n1"), asyncio.create_task(func2(), name="n2")]

    print("任务结束")

    done, pending = await asyncio.wait(task_list, timeout=2)

    print("已完成：", done)
    print("未完成:", pending)
    print(done)


# asyncio.run(main2())

# Future
# 示例1

async def main3():
    # 获取当前时间循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（Future对象）, 这个任务什么也不干
    fut = loop.create_future()

    # 等待任务最终结果， 没有结果则会一直等待下去
    await fut

# asyncio.run(main3()) # 会一直执行下去

# 示例2

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result("666")

async def main4():
    # 获取当前时间循环
    loop = asyncio.get_running_loop()

    # 创建一个任务
    fut = loop.create_future()

    # 创建一个任务，绑定set_after对象
    await loop.create_task(set_after(fut))

    # 等待任务返回结果
    data = await fut

    print(data)

asyncio.run(main4())
