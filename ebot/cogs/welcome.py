from string import Template

import discord
from discord.ext import commands
from discord.ext.commands.context import Context

from ..db.crud import get_config_value

DEFAULT_WELCOME_MSG = Template(
    "Everyone welcome, $member to the server! " +
    "We hope you enjoy your time here."
)

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            message = get_config_value("welcome-msg")
            if message:
                message = Template(message)
            else:
                message = DEFAULT_WELCOME_MSG

            await channel.send(message.safe_substitute(member=member.mention))


async def init(bot):
    await bot.add_cog(Welcome(bot))
