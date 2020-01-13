import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

def set_result_to_future(value, future):
    if not future.done():
        future.set_result(value)

loop = asyncio.get_event_loop()
loop.set_debug(True)
future = loop.create_future()
loop.call_soon(set_result_to_future, 'DONE!', future)
result = loop.run_until_complete(future)
assert(future.result() == result)
print(result)
loop.close()
