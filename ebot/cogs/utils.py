import asyncio
import secrets

from discord import app_commands, Interaction
from discord.ext.commands import GroupCog


class Utils(GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="count-down", description="A count down, max of 10 seconds")
    async def count_down(
            self,
            interaction: Interaction,
            secs: int,
            title: str = "Count-Down",
            end_msg: str = "Timer Elapsed!!!"):
        secs = min(secs, 10)

        # supporting both server & dm
        msg_dst = interaction.channel or interaction.user

        await interaction.response.send_message("starting countdown...", ephemeral=True)

        while secs > 0:
            await msg_dst.send(f"*{title}*\n{secs} seconds left!")
            secs -=1
            await asyncio.sleep(1)

        await msg_dst.send(end_msg)

    @app_commands.command(name="reversed", description="reverses your message")
    async def reversed(self, interaction: Interaction, msg: str, sep: str = ""):
        reversed_ = sep.join(reversed(msg))
        await interaction.response.send_message(f"`{msg}` >>> `{reversed_}`", ephemeral=True)


async def init(bot):
    await bot.add_cog(Utils(bot))
