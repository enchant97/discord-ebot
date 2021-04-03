from discord.ext import commands
from discord.ext.commands.context import Context
import logging

logger = logging.getLogger(__name__)


class OwnerCog(commands.Cog):
    """
    commands that only the bot owner can use
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="isowner", hidden=True)
    @commands.is_owner()
    async def is_owner(self, ctx: Context):
        await ctx.send(f'Hello {ctx.author.mention}. You are the owner!')

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        logger.info(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')


def setup(bot):
    bot.add_cog(OwnerCog(bot))
