'''
https://docs.python.org/ja/3.6/library/asyncio-task.html#example-chain-coroutines
'''
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

async def compute(x, y):
    print("Compute %s + %s" % (x, y))
    await asyncio.sleep(5.0)
    return x + y

async def print_sum(x, y):
    r = await compute(x, y)
    print("Result of compute(): %s + %s = %s" % (x, y, r))

loop = asyncio.get_event_loop()
loop.set_debug(True)
loop.run_until_complete(print_sum(1, 2))
loop.close()
