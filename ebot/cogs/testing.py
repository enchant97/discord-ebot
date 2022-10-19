import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class TestingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx: Context, *, member: discord.Member = None):
        await ctx.reply("pong!")
