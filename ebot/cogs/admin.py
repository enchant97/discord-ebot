from string import Template

import discord
from discord import app_commands, Interaction
from discord.ext import commands
from discord.ext.commands.context import Context

from ..db.crud import get_config_value, set_config_value


class ManageSelectableRolesSelect(discord.ui.RoleSelect):
    async def callback(self, interaction: Interaction):
        set_config_value(
            interaction.guild.id,
            "member-selectable-roles",
            [str(role.id) for role in self.values],
        )
        await interaction.response.edit_message(content="Set new roles", view=None)


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
        if message:
            message = Template(message).safe_substitute(member=ctx.author.mention)
            await ctx.reply(message, ephemeral=True)
        else:
            await ctx.reply("no welcome message has been set", ephemeral=True)

    @app_commands.command(name="selectable-roles", description="set user selectable roles (reaction roles)")
    async def selectable_roles(self, interaction: Interaction):
        view = discord.ui.View()
        view.add_item(ManageSelectableRolesSelect(max_values=25))
        await interaction.response.send_message(
            "Select roles to enable",
            view=view,
            ephemeral=True
        )


async def init(bot):
    await bot.add_cog(Admin(bot))
