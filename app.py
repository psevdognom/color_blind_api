import argparse

from aiohttp import web
# import aiomonitor

from views import routes as view_routes



async def make_app(middleware=None):
    app = web.Application(client_max_size=50*10485760
    )
    app.router.add_routes([*view_routes])
    # запись логов в бд
    # await log_db.set_bind(f'postgresql+asyncpg://{a.DB_LOGS_USR}:{a.DB_LOGS_PASSWORD}@{a.DB_LOGS_HOST}/{a.DB_LOGS_NAME}')
    return app



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API Server. Colorblind\n')
    parser.add_argument('host', nargs='?', default='0.0.0.0', help='IP adress of api server')
    parser.add_argument('-p', '--port', nargs='?', default='8080', help='listening port')
    args = parser.parse_args()
    web.run_app(make_app(), host=args.host, port=args.port)
