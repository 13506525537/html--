import asyncio

class AsyncContextManager:
    def __init__(self):
        self.conn = None


    async def do_something(self):
        # 异步操作数据库
        return 666

    async def __aenter__(self):
        # 异步连接数据库
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭数据库
        await asyncio.sleep(1)


async def func():
    async with AsyncContextManager() as f:
        result = await f.do_something()
        print(result)

asyncio.run(func())


# 可以在最前面加上, 能将asynico默认循环替换为uvloop循环，提升效率
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
