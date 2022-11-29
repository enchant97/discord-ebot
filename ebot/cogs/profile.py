import discord
from discord import app_commands, Interaction
from discord.ext import commands
from discord.errors import Forbidden

from ..db.crud import get_config_value, set_config_value


class SelectableRolesSelect(discord.ui.Select):
    def __init__(self, roles: tuple[discord.Role]):
        self._roles = roles
        options = [discord.SelectOption(label=role.name, value=str(role.id)) for role in roles]
        super().__init__(options=options, max_values=len(options))

    async def callback(self, interaction: Interaction):
        try:
            await interaction.user.remove_roles(*self._roles, reason="profile customisation")
            roles_to_add = map(lambda id_:interaction.guild.get_role(int(id_)), self.values)
            await interaction.user.add_roles(*roles_to_add, reason="profile customisation")
            await interaction.response.edit_message(content="Updated your roles", view=None)
        except Forbidden:
            await interaction.response.edit_message(
                content="Unable to update roles, does bot have permission?")


@app_commands.guild_only()
class Profile(commands.GroupCog):
    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="set-roles", description="set your profile roles")
    async def set_roles(self, interaction: Interaction):
        selectable_role_ids = get_config_value(
            interaction.guild.id,
            "member-selectable-roles",
        )

        if selectable_role_ids is None or len(selectable_role_ids) == 0:
            await interaction.response.send_message(
                "No user selectable roles available",
                ephemeral=True,
            )
            return

        # convert role id's into Role obj's
        roles_for_selection = map(lambda id_:interaction.guild.get_role(int(id_)), selectable_role_ids)
        # remove roles not found
        roles_for_selection = tuple(filter(lambda x:x, roles_for_selection))

        view = discord.ui.View()
        view.add_item(SelectableRolesSelect(roles=roles_for_selection))
        await interaction.response.send_message(
            "Select Your Roles",
            view=view,
            ephemeral=True
        )


async def init(bot):
    await bot.add_cog(Profile(bot))
