import asyncio
import aioredis

async def execute(address):
    print("开始链接", address)

    redis = await aioredis.from_url(address)

    async with redis.client() as conn:
        await conn.set("my_key", 1)
        val = await conn.get("my_key")
    print(val)
    return val


if __name__ == '__main__':
    task_list=[execute("redis://localhost/0"), execute("redis://localhost/0")]
    a = asyncio.run(asyncio.wait(task_list))
    print(a)
