import asyncio


class Reader(object):
    """自定义异步迭代器（同时也是异步可迭代对象）"""

    def __init__(self):
        self.count = 0

    async def readline(self):
        self.count += 1
        if self.count == 100:
            return
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.readline()
        if val == None:
            raise StopAsyncIteration

        return val

if __name__ == '__main__':

    async def fun():
        read = Reader()

        async for item in read:
            print(item)

    asyncio.run(fun())
    
