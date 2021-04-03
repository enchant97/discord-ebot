from functools import cache
from typing import List

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str = "sqlite://:memory:"
    LOG_LEVEL: str = "WARNING"
    PREFIXES: List[str] = ["!"]
    DESCRIPTION: str = "The bot that runs on the \
Enchanted People discord server"
    TOKEN: str

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


@cache
def get_settings():
    return Settings()
