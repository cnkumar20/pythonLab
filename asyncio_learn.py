import asyncio
import time
from collections import deque
async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(3, 'hello')
    await say_after(1, 'world')

    print(f"finished at {time.strftime('%X')}")
    names = deque(['hammer', 'check'])
    for r in names:
        print(f"{r}")
asyncio.run(main())
