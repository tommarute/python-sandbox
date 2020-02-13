from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route('/')
async def test(request):
    return json({'hello': 'sanic'})


if __name__ == '__main__':
    app.run(
        host='0.0.0.0', port=8000, debug=True, ssl=None, sock=None,
        workers=1, protocol=None, backlog=1000, stop_event=None,
        register_sys_signals=True, access_log=None)
