from rethinkdb import r

from .utils import get_conn


def get_config_value(key: str):
    return r.table("config").get(key).run(get_conn())


def set_config_value(key: str, value):
    r.table("config").insert(
        {"id": key, "value": value},
        conflict="replace"
    ).run(get_conn())
