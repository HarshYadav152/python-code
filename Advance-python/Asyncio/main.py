import time
import asyncio

async def function1():
    await asyncio.sleep(1)
    print("function 1")

async def function2():
    await asyncio.sleep(1)
    print("function 2")

async def function3():
    await asyncio.sleep(3)
    print("function 3")
    return "HArsh"

async def main():
    # task = asyncio.create_task(function1())
    L = await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)

asyncio.run(main())