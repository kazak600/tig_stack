import logging
from aiohttp import web
from datetime import datetime
from pymongo import MongoClient

routes = web.RouteTableDef()


@routes.get('/')
async def index(request):
    db = request.app['db'].client.tig
    db.hits.insert_one({'ts': datetime.now()})
    return web.json_response({'status': 'OK'})


def main():
    app = web.Application()
    app.add_routes(routes)
    app['db'] = getattr(MongoClient(host='mongodb', port=27017, username='admin', password='admin'), 'tig')

    logging.basicConfig(level=logging.DEBUG)
    web.run_app(app)


if __name__ == '__main__':
    main()
