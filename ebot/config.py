from functools import cache
from typing import List, Tuple

from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_URI: str = "sqlite://:memory:"
    LOG_LEVEL: str = "WARNING"
    PREFIXES: List[str] = ["!"]
    DESCRIPTION: str = "The bot that runs on the \
Enchanted People discord server"
    TOKEN: str
    USER_EXPIRES: str = "2m"
    RUN_AUTO_CLEANUPS: bool = True

    def get_expire_time(self) -> Tuple[int, str]:
        expire_val = int(self.USER_EXPIRES[:-1])
        expire_sel = self.USER_EXPIRES[-1].lower()
        if expire_sel not in ("d", "w", "m", "y"):
            raise ValueError("invalid USER_EXPIRES value")
        return expire_val, expire_sel

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'


@cache
def get_settings():
    return Settings()
