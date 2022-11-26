import secrets

from discord.ext import commands
from discord.ext.commands.context import Context


class Games(commands.GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.hybrid_command(name="coin-flip", description="flip a coin")
    async def coin_flip(self, ctx: commands.Context):
        result = secrets.choice((":coin: Heads!", ":coin: Tail!"))
        await ctx.reply(result)

    @commands.hybrid_command(
        name="random-number",
        description="generate a random number from given range")
    async def random_number(self, ctx: commands.Context, start: int, end: int):
        result = secrets.choice(range(start, end+1))
        await ctx.reply(f"Picked: {result}")

async def init(bot):
    await bot.add_cog(Games(bot))
