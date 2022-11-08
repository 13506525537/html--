import asyncio
import requests

async def download_image(url):
    # "发送网络请求下载图片"
    print("开始下载：",url)

    loop = asyncio.get_running_loop()
    # requests模块不支持异步，所以使用线程池来配合实现
    fut = loop.run_in_executor(None, requests.get, url)

    response = await fut
    print("下载完成")

    # 将图片保存到本地
    file_name = url.rsplit("=")[-1] + ".jpg"
    with open(file_name, mode="wb") as file_object:
        file_object.write(response.content)


if __name__ == '__main__':
    url_list = [
        "https://img1.baidu.com/it/u=158661084,3496043317&fm=253&fmt=auto&app=120&f=JPEG?w=1281&h=800",
        "https://img0.baidu.com/it/u=1621175510,2896751425&fm=253&fmt=auto&app=138&f=JPEG?w=333&h=500",
        "https://img0.baidu.com/it/u=3183938376,2047122145&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=1082",
        "https://img1.baidu.com/it/u=739531633,2491792678&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=719"
    ]

    tasks = [download_image(url) for url in url_list]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))

