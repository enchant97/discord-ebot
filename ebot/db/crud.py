from rethinkdb import r

from .utils import get_conn


def get_config_value(key: str):
    return r.table("config").get(key).run(get_conn())
