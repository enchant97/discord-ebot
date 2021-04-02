from discord.ext import commands

from .config import get_settings


class Bot(commands.Bot):
    """
    subclass of the discord.py Bot class
    """
    def load_extentions(self, names) -> None:
        for name in names:
            self.load_extension(name)


def get_prefix(bot, message):
    prefixes = get_settings().PREFIXES

    if not message.guild:
        # Only allow ? to be used in DMs
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)
