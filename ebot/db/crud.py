from rethinkdb import r
from rethinkdb.errors import ReqlNonExistenceError

from .utils import get_conn


def get_config_value(guild_id: int, key: str):
    try:
        return r.table("config").get(guild_id)[key].run(get_conn())
    except ReqlNonExistenceError:
        pass


def set_config_value(guild_id: int, key: str, value):
    r.table("config").insert(
        {"guild_id": guild_id, key: value},
        conflict="update"
    ).run(get_conn())


def insert_idea(guild_id: int, author_id: int, idea: str):
    r.table("ideas").insert(
        {"guild_id": guild_id, "author_id": author_id, "created_at": r.now(), "idea": idea},
    ).run(get_conn())


def get_ideas_latest(guild_id: int, limit: int):
    return r.table("ideas") \
        .filter({"guild_id": guild_id}) \
        .order_by(r.desc('created_at')) \
        .limit(limit) \
        .run(get_conn())
