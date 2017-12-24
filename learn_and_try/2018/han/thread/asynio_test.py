import asyncio


async def world():
    print("star->>")
    r = await asyncio.sleep(1)
    print("World")


async def hello():
    print("Hello")


loop = asyncio.get_event_loop()
#实现函数并发执行
tasks = [world(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

