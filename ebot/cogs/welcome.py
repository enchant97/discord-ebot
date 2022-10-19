import discord
from discord.ext import commands
from discord.ext.commands.context import Context


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send(
                f"Everyone welcome, {member.mention} to the server!" +
                "We hope you enjoy your time here."
            )


async def init(bot):
    await bot.add_cog(Welcome(bot))
