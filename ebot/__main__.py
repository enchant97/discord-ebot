import asyncio
import logging
import os
import sys

from .main import create_bot

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    token = os.environ.get("DISCORD_TOKEN")

    if not token:
        sys.exit("no api token set, use 'DISCORD_TOKEN'")

    bot = asyncio.run(create_bot())
    bot.run(token)
