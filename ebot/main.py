import discord
from discord.ext import commands

from . import cogs


async def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(
        command_prefix="?",
        intents=intents
    )

    await bot.add_cog(cogs.TestingCog(bot))

    return bot
