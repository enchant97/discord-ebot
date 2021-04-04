import logging

from discord.ext import commands, tasks
from discord.ext.commands.context import Context

from ..config import get_settings
from ..database import crud

logger = logging.getLogger(__name__)


class OwnerCog(commands.Cog):
    """
    commands that only the bot owner can use
    """
    def __init__(self, bot):
        self.bot = bot

        if get_settings().RUN_AUTO_CLEANUPS:
            self.auto_cleanup.start()
        else:
            logger.info("not starting auto-cleanup as disabled in settings")

    @commands.command(name="isowner", hidden=True)
    @commands.is_owner()
    async def is_owner(self, ctx: Context):
        await ctx.send(f'Hello {ctx.author.mention}. You are the owner!')

    @commands.command("cleanup", hidden=True)
    @commands.is_owner()
    async def cleanup(self, ctx: Context):
        """
        run a database cleanup, removing old users
        that haven't sent a message to the bot in a while
        """
        logger.info("manual cleanup triggered by %s", ctx.author)
        await crud.cleanup()
        await ctx.send(
            "manual cleanup triggered",
            reference=ctx.message)

    @commands.Cog.listener()
    async def on_member_ban(self, guild, user):
        logger.info(f'{user.name}-{user.id} was banned from {guild.name}-{guild.id}')

    @tasks.loop(hours=24)
    async def auto_cleanup(self):
        logger.info("auto cleanup triggered")
        await crud.cleanup()

    @auto_cleanup.before_loop
    async def before_auto_cleanup(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(OwnerCog(bot))
