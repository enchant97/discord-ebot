from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from .utils import get_conn


def get_config_value(guild_id: int, key: str):
    try:
        return r.table("config").get(guild_id)[key].run(get_conn())
    except:
        pass


def set_config_value(guild_id: int, key: str, value):
    r.table("config").insert(
        {"id": guild_id, key: value},
        conflict="update"
    ).run(get_conn())
