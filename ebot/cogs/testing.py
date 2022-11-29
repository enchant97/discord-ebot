from discord.ext.commands import GroupCog
from discord import app_commands, Interaction


class Testing(GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(description="bot replies with 'pong'")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message("pong!", ephemeral=True)


async def init(bot):
    await bot.add_cog(Testing(bot))
