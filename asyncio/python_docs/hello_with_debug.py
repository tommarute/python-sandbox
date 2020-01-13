'''
https://docs.python.org/ja/3.6/library/asyncio-dev.html#debug-mode-of-asyncio
'''
import asyncio
import logging

logging.basicConfig(level=logging.DEBUG)

def hello_world(loop):
    loop.set_debug(True)
    print('Hello World')
    loop.stop()

loop = asyncio.get_event_loop()

# Schedule a call to hello_world()
loop.call_soon(hello_world, loop)

# Blocking call interrupted by loop.stop()
loop.run_forever()
loop.close()
