from string import Template
import secrets

import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands.context import Context

from ..db.crud import get_config_value, set_config_value


@app_commands.guild_only()
class Admin(commands.GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.hybrid_command(name="welcome-msg", description="set or get the welcome message")
    async def welcome_msg(self, ctx: commands.Context, new_message: str | None = None):
        if new_message:
            set_config_value(ctx.guild.id, "welcome-msg", new_message)
        message = new_message or get_config_value(ctx.guild.id, "welcome-msg")
        print(message)
        if message:
            message = Template(message).safe_substitute(member=ctx.author.mention)
            await ctx.reply(message)
        else:
            await ctx.reply("no welcome message has been set")


async def init(bot):
    await bot.add_cog(Admin(bot))
