from string import Template

from discord import app_commands, Interaction, Member
from discord.ext.commands import Cog

from ..db.crud import get_config_value

DEFAULT_WELCOME_MSG = Template(
    "Everyone welcome, $member to the server! " +
    "We hope you enjoy your time here."
)

class Welcome(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_member_join(self, member: Member):
        channel = member.guild.system_channel
        if channel is not None:
            message = get_config_value(member.guild.id, "welcome-msg")
            if message:
                message = Template(message)
            else:
                message = DEFAULT_WELCOME_MSG

            await channel.send(message.safe_substitute(member=member.mention))

    @app_commands.command(description="show the credits for the bot")
    async def credits(self, interaction: Interaction):
        await interaction.response.send_message(
            "Powered By [ebot](https://github.com/enchant97/discord-ebot), " +
            "the official Enchanted People discord bot", ephemeral=True)


async def init(bot):
    await bot.add_cog(Welcome(bot))
