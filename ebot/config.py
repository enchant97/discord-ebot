from functools import cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str = "sqlite://:memory:"
    LOG_LEVEL: str = "WARNING"
    PREFIX: str = "!ebot"
    DESCRIPTION: str = "the bot that runs on the \
        Enchanted People discord server"
    TOKEN: str

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


@cache
def get_settings():
    return Settings()
