import discord

from .bot import Bot
from .config import get_settings

cogs = [
    "ebot.cogs.owner",
]

bot = Bot(
    command_prefix=get_settings().PREFIX,
    description=get_settings().DESCRIPTION,
    )

bot.load_extentions(cogs)


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name} - {bot.user.id}")
    print(f"Discord Version: {discord.__version__}")
    print("bot now ready...")
