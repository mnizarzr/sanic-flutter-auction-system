import logging
import os
import aioredis
from sanic import Sanic
from sanic.response import text
from sanic_motor import BaseModel

from config.app_config import AppConfig

app = Sanic(__name__)

app.update_config(AppConfig)

BaseModel.init_app(app)

@app.get("/")
async def hello_world(request):
    return text("Hello, world.")


@app.before_server_start
async def before_server_start(appop):
    _redis_url = app.config.get("REDIS_URL")
    try:
        _redis = await aioredis.from_url(_redis_url)
    except ConnectionError:
        logging.error("Redis connection error")
        app.stop()
        exit(1)
    setattr(app.ctx, "redis", _redis)


@app.after_server_stop
async def after_server_stop():
    logging.info(f'[redis] closing connection')
    app.ctx.redis.close()

if __name__ == '__main__':
    app.run(debug=os.getenv("DEBUG", False),
            host=os.getenv("HOST", "127.0.0.1"),
            port=os.getenv("PORT", 8000))
