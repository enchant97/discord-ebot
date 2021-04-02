from discord.ext.commands import Bot as _Bot


class Bot(_Bot):
    """
    subclass of the discord.py Bot class
    """
    def load_extentions(self, names) -> None:
        for name in names:
            self.load_extension(name)
