from discord.ext import commands
from discord.ext.commands.context import Context


class Testing(commands.GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.hybrid_command(description="bot replies with 'pong'")
    async def ping(self, ctx: commands.Context):
        await ctx.reply("pong!", ephemeral=True)


async def init(bot):
    await bot.add_cog(Testing(bot))
