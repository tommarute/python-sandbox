'''
https://docs.python.org/ja/3.6/library/asyncio-task.html#example-coroutine-displaying-the-current-date
'''
import asyncio
import datetime
import logging

logging.basicConfig(level=logging.DEBUG)

async def display_date(loop):
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.set_debug(True)
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop))
loop.close()
