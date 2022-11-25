from string import Template

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from ..db.crud import get_config_value


class Testing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.hybrid_command(description="bot replies with 'pong'")
    async def ping(self, ctx: commands.Context):
        await ctx.reply("pong!")

    @commands.hybrid_command(description="output welcome message")
    async def welcome(self, ctx: commands.Context):
        message = get_config_value("welcome-msg")
        if message:
            message = Template(message["value"]).safe_substitute(member=ctx.author.mention)
        else:
            message = "no welcome message has been set..."

        await ctx.reply(message)


async def init(bot):
    await bot.add_cog(Testing(bot))
