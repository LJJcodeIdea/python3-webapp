import asyncio
from aiohttp import web
import nest_asyncio

#处理 IPython/ipykernel 不支持 asyncio 的问题
nest_asyncio.apply()

async def hello(request):
    return web.Response(text="Hello World",content_type='text/html')

async def init():
    server = web.Server(hello)
    runner = web.ServerRunner(server)
    await runner.setup()
    site = web.TCPSite(runner,'localhost',8083)
    await site.start()
    await asyncio.sleep(100*3600)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(init())
except KeyboardInterrupt:
    pass
loop.close()
