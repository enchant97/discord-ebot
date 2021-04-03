import discord
from tortoise import Tortoise

from .bot import Bot, get_prefix
from .config import get_settings
from .database import models

cogs = [
    "ebot.cogs.owner",
    "ebot.cogs.life_sim",
    "ebot.cogs.game",
]

bot = Bot(
    command_prefix=get_prefix,
    description=get_settings().DESCRIPTION,
    )


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name} - {bot.user.id}")
    print(f"Discord Version: {discord.__version__}")
    print("bot now ready...")


async def init_db():
    await Tortoise.init(
        db_url=get_settings().DB_URI,
        modules={'models': [models],
        }
    )
    await Tortoise.generate_schemas()
