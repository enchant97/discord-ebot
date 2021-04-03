import logging
import random

from discord.ext import commands
from discord.ext.commands.context import Context

logger = logging.getLogger(__name__)


class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command("coinflip", aliases=["flip"])
    async def coin_flip(self, ctx: Context):
        """
        flip a coin and return either 'heads' or 'tails'
        """
        coin_side = random.choice(["Heads", "Tails"])
        logger.info(
            "%s asked me to flip a coin, I got '%s'",
            ctx.author,
            coin_side)
        await ctx.send(
            f"Got '{coin_side}'",
            reference=ctx.message)


def setup(bot):
    bot.add_cog(Games(bot))
