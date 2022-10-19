import os
import asyncio

from .main import create_bot

if __name__ == "__main__":
    bot = asyncio.run(create_bot())
    bot.run(os.environ.get("DISCORD_TOKEN"))
