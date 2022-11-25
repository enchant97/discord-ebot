from os import environ

from rethinkdb import r
from rethinkdb.errors import RqlRuntimeError

shared_conn = None


def get_conn():
    if shared_conn is None:
        raise ValueError("database connection must be setup")
    return shared_conn


def init_connection():
    global shared_conn
    # TODO use async mode, when it's fixed for python 3.10
    connection = r.connect(
        host=environ.get("DB_HOST", "127.0.0.1"),
        port=int(environ.get("DB_PORT", "28015")),
        db=environ.get("DB_DB", "ebot"),
        user=environ.get("DB_USER", "admin"),
        password=environ.get("DB_PASS", ""),
    )

    try:
        r.table_create("config").run(connection)
    except RqlRuntimeError:
        pass

    shared_conn = connection

    return connection
