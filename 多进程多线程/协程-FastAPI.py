import asyncio
import uvicorn
from fastapi import FastAPI
import aioredis
import requests

app = FastAPI()


# redis = aioredis.ConnectionPool.from_url()
# conn = redis.client()

@app.get("/")
def index():
    """普通接口"""
    # 某个IO操作10s
    return {"message": "hello world"}


@app.get("/read")
async def read():
    """异步接口"""
    print("请求来了")
    await asyncio.sleep(10)
    print("执行结束了")
    return "等待了10s"


if __name__ == '__main__':
    result = uvicorn.run("协程-FastAPI:app", host="127.0.0.1", port=5000, log_level="info")
    print(result)
    print("1111")
