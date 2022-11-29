from discord import app_commands, Interaction
from discord.ext.commands import GroupCog

from ..db.crud import insert_idea, get_ideas_latest


@app_commands.guild_only()
class IdeaBox(GroupCog, group_name="idea-box"):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(description="add a suggestion")
    async def add(self, interaction: Interaction, idea: str):
        insert_idea(interaction.guild.id, interaction.user.id, idea)
        await interaction.response.send_message("That's a great idea!", ephemeral=True)

    @app_commands.command(description="get the latest suggestions")
    async def latest(self, interaction: Interaction, limit: int | None = 5):
        latest_ideas = get_ideas_latest(interaction.guild.id, min(limit, 20))
        output = "Ideas:"
        for idea in latest_ideas:
            output += f"\n- {idea['idea']}"
            if (author := self.bot.get_user(int(idea["author_id"]))) is not None:
                output += f" by {author.mention}"
        await interaction.response.send_message(output, ephemeral=True)


async def init(bot):
    await bot.add_cog(IdeaBox(bot))
