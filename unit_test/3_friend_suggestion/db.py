import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    db = sqlite3.connect('./persons.db', detect_types=sqlite3.PARSE_DECLTYPES)
    return db


def close_db(e=None):
    """If this request connected to the database, close the
    connection.
    """
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    """Clear existing data and create new tables."""
    db = get_db()

    with open("./schema.sql") as f:
        db.executescript(f.read())


def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


if __name__ == '__main__':
    init_db_command()

    # conn = sqlite3.connect('./persons.db')
    # c = conn.cursor()
    # for row in c.execute('SELECT * FROM persons'):
    #     print(row)

