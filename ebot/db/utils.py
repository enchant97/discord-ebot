from os import environ

from rethinkdb import r
from rethinkdb.errors import RqlRuntimeError

shared_conn = None


def get_conn():
    if shared_conn is None:
        raise ValueError("database connection must be setup")
    return shared_conn


def _create_table(conn, name: str, **kw):
    try:
        r.table_create(name, **kw).run(conn)
    except RqlRuntimeError:
        pass


def init_connection():
    global shared_conn
    # TODO use async mode, when it's fixed for python 3.10
    connection = r.connect(
        host=environ.get("DB_HOST", "127.0.0.1"),
        port=int(environ.get("DB_PORT", "28015")),
        db=environ.get("DB_DB", "test"),
        user=environ.get("DB_USER", "admin"),
        password=environ.get("DB_PASS", ""),
    )

    _create_table(connection, "config", primary_key="guild_id")
    _create_table(connection, "ideas")

    shared_conn = connection

    return connection
