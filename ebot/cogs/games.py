import secrets

from discord import app_commands, Interaction
from discord.ext.commands import GroupCog


class Games(GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="coin-flip", description="flip a coin")
    async def coin_flip(self, interaction: Interaction):
        result = secrets.choice((":coin: Heads!", ":coin: Tail!"))
        await interaction.response.send_message(result)

    @app_commands.command(
        name="random-number",
        description="generate a random number from given range")
    async def random_number(self, interaction: Interaction, start: int, end: int):
        result = secrets.choice(range(start, end+1))
        await interaction.response.send_message(f"Picked ({start}-{end}): {result}")

async def init(bot):
    await bot.add_cog(Games(bot))
