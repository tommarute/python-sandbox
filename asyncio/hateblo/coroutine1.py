import asyncio
import logging
import sys

fmt = '[%(asctime)s] [%(levelname)s] (%(filename)s:%(lineno)d):' +\
    '%(funcName)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, format=fmt)

async def boring_counting(id_, n):
    for i in range(n):
        print('eh, I am {}. {} :('.format(id_, i))
        await asyncio.sleep(1.0)
    print('FINISH! by {} :)'.format(id_))

def get_input():
    try:
        n = int(sys.argv[1])
    except IndexError:
        print('Input an integer.')
        n = int(input())

    if n < 1:
        n = 1

    return n

n = get_input()
loop = asyncio.get_event_loop()
loop.set_debug(True)
futures = set()
for i in range(5):
    futures.add(boring_counting(i, n))

loop.run_until_complete(asyncio.wait(futures))
loop.close()
