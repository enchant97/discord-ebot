from .config import get_settings
from .main import bot

if __name__ == "__main__":
    bot.run(
        get_settings().TOKEN,
        bot=True,
        reconnect=True,
        )
