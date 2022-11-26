from rethinkdb import r

from .utils import get_conn


def get_config_value(guild_id: int, key: str):
    return r.table("config").get(guild_id)[key].run(get_conn())


def set_config_value(guild_id: int, key: str, value):
    r.table("config").insert(
        {"id": guild_id, key: value},
        conflict="update"
    ).run(get_conn())
