import asyncio

from tortoise import Tortoise

from .config import get_settings
from .main import bot, init_db

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                bot.start(
                    get_settings().TOKEN,
                    bot=True,
                    reconnect=True,
                ),
                init_db(),
                loop=loop,
            )
        )
    except KeyboardInterrupt:
        loop.run_until_complete(bot.logout())
        loop.run_until_complete(Tortoise.close_connections())
    finally:
        loop.close()
