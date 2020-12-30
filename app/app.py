import argparse

from aiohttp import web

from tortoise import Tortoise

from app import auth

async def on_start(app):  # NOQA
    await Tortoise.init(
        db_url=f"postgres://{auth.USER}:{auth.PASSWORD}@{auth.HOST}/{auth.DATABASE}",
        modules={'models': ['seller.test.models']}
    )


async def on_shutdown(app):  # NOQA
    await Tortoise.close_connections()

def make_app():
    app = web.Application(
    )
    # app.router.add_routes([*view_routes])
    # app[s.LOGGING_TYPE] = s.LOG_TYPE_DEBUG
    # await db.set_bind(f'postgresql+asyncpg://{a.DB_USR}:{a.DB_PASSWORD}@{a.DB_HOST}/{a.DB_NAME}')
    # запись логов в бд
    # await log_db.set_bind(f'postgresql+asyncpg://{a.DB_LOGS_USR}:{a.DB_LOGS_PASSWORD}@{a.DB_LOGS_HOST}/{a.DB_LOGS_NAME}')
    app.on_startup.append(on_start)
    app.on_shutdown.append(on_shutdown)
    return app


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='API Server. API server MileOnAir Loyalty Programs\n')
    parser.add_argument('host', nargs='?', default='0.0.0.0', help='IP adress of api server')
    parser.add_argument('-p', '--port', nargs='?', default='8080', help='listening port')
    args = parser.parse_args()
    web.run_app(make_app(), host=args.host, port=args.port)