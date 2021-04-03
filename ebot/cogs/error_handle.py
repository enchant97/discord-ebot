import logging
import sys
import traceback

from discord.ext import commands
from discord.ext.commands.context import Context

logger = logging.getLogger(__name__)


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):
        """
        triggered when an error occurs
        while invoking a command
        """
        if hasattr(ctx.command, 'on_error'):
            return

        if isinstance(error, commands.CommandNotFound):
            logger.debug("%s caused is unknown", ctx.command)
            await ctx.send(
                f"command {ctx.command} is unknown",
                reference=ctx.message)
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(
                f"command {ctx.command} is disabled",
                reference=ctx.message)
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.author.send(f"{ctx.command} cannot be used \
in Private Messages")
        else:
            traceback.print_exception(
                type(error), error,
                error.__traceback__, file=sys.stderr)
            await ctx.send(
                "The command caused an unknown error",
                reference=ctx.message)


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
