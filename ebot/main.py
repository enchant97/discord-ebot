import importlib
import logging
import os
import sys

import discord
from discord.ext import commands

from .db.utils import init_connection

logger = logging.getLogger("ebot")


async def create_bot():
    enabled_cogs = os.environ.get("ENABLED_COGS")

    if not enabled_cogs:
        sys.exit("at least one cog must be enabled, use 'ENABLED_COGS' to set them")

    enabled_cogs = enabled_cogs.split(",")

    db_conn = init_connection()

    intents = discord.Intents.all()
    intents.message_content = False
    intents.members = True

    bot = commands.Bot(
        command_prefix=os.environ.get("COMMAND_PREFIX", "!e"),
        intents=intents,
        strip_after_prefix=True,
    )

    # setup all enabled cogs, including external ones
    for cog_name in enabled_cogs:
        logger.info("loading '%s' cog", cog_name)
        if cog_name.startswith("."):
            # built-in cog
            await importlib.import_module(cog_name, "ebot.cogs").init(bot)
        else:
            # external cog (from a plugin)
            await importlib.import_module(cog_name).init(bot)

    @bot.event
    async def on_ready():
        # sync slash-commands
        await bot.tree.sync()

    return bot
