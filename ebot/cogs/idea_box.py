from discord import app_commands
from discord.ext import commands
from discord.ext.commands.context import Context

from ..db.crud import insert_idea, get_ideas_latest


@app_commands.guild_only()
class IdeaBox(commands.GroupCog, group_name="idea-box"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.hybrid_command(description="add a suggestion")
    async def add(self, ctx: commands.Context, idea: str):
        insert_idea(ctx.guild.id, ctx.author.id, idea)
        await ctx.reply("That's a great idea!", ephemeral=True)

    @commands.hybrid_command(description="get the latest suggestions")
    async def latest(self, ctx: commands.Context, limit: int | None = 5):
        latest_ideas = get_ideas_latest(ctx.guild.id, min(limit, 20))
        output = "Ideas:"
        for idea in latest_ideas:
            output += f"\n- {idea['idea']}"
        await ctx.reply(output, ephemeral=True)


async def init(bot):
    await bot.add_cog(IdeaBox(bot))
