import asyncio
import aiohttp


async def fetch(session, url):
    print("发送请求", url)
    try:
        async with session.get(url, verify_ssl=False) as response:
            text = await response.text()
            print("得到结果", url, len(text))
            return text
    except Exception as e:
        print(e)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://python.org',
            'https://www.baidu.com',
            'https://www.pythonav.com'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

        done, pending = await asyncio.wait(tasks)
        return done, pending


if __name__ == '__main__':
    done, pending = asyncio.run(main())
    print(1, done)
    print(2, pending)
