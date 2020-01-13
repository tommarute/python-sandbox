import asyncio
import logging
import sys
from random import randint

logging.basicConfig(level=logging.DEBUG)

def random_hit(future, n_upper, count=1, loop=None):
    if loop is None:
        loop = asyncio.get_event_loop()
    value = randint(1, n_upper)
    if value == n_upper:
        print('Hit!')
        future.set_result(count)
    else:
        print('Not yet.')
        count += 1
        loop.call_soon(random_hit, future, n_upper, count, loop)

def eternal_hello(loop):
    print('Hello!')
    loop.call_soon(eternal_hello, loop)

def _callback(future):
    print('Done!')
    loop = asyncio.get_event_loop()

try:
    n = int(sys.argv[1])
except IndexError:
    print('Input an integer.')
    n = int(input())

if n < 1:
    n = 1

loop = asyncio.get_event_loop()
loop.set_debug(True)
future = loop.create_future()
future.add_done_callback(_callback)
loop.call_soon(random_hit, future, n)
loop.call_soon(eternal_hello, loop)
result = loop.run_until_complete(future)
print(result)
loop.close()
