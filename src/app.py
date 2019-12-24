import asyncio
from aiohttp import web
import aiohttp
import logging
import util as ut
import config as conf

async def fetch(client, method, path, headers, body):
    baseUrl = conf.base_url
    if len(path) > 1:
        baseUrl = baseUrl + path

    async with client.request(
        method, baseUrl, headers=ut.cdic_to_dic(headers), data=body
    ) as response:
        body_result = await response.text()
        return body_result, ut.cdic_to_dic(response.headers)


async def index(request):
    async with aiohttp.ClientSession() as client:
        logging.info("=======================INFO===============================")
        print("--------------------------request----------------------")
        response_body, response_header = await fetch(
            client,
            request.method,
            request.path_qs,
            request.headers,
            await request.read(),
        )

        return web.Response(text=response_body, headers=ut.filter_not_permited_headers(response_header))

async def webapp():
    loop = asyncio.get_event_loop()
    app = web.Application(loop=loop)
    app.router.add_route("*", "/{path:.*}", index)
    return app


if __name__ == '__main__':
    print("=================run Localy just for debug====================")
    web.run_app(webapp(), host='localhost', port=9000)
