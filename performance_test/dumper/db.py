import sqlite3

import click
from flask import current_app
from flask import g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    """Connect to the application's configured database. The connection
    is unique for each request and will be reused if this is called
    again.
    """
    db = sqlite3.connect('./flaskr.sqlite', detect_types=sqlite3.PARSE_DECLTYPES)
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

    # Create tables
    with open("./schema.sql") as f:
        db.executescript(f.read())

    # Create user
    username = 'demo'
    password = 'demo'
    db = get_db()
    error = None

    db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)",
        (username, generate_password_hash(password)),
    )
    db.commit()

    row = db.execute("SELECT id FROM user WHERE username = ?", (username,)).fetchone()
    u_id = row[0]

    # Import data
    with open('news.csv', 'r') as f:
        for line in f:
            p = line.split(',')
            db.execute("INSERT INTO post (author_id, title, body) VALUES (?, ?, ?)", (u_id, p[0], p[1])).fetchone()
            db.commit()
            # print(line)


def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


if __name__ == '__main__':
    init_db_command()

    # conn = sqlite3.connect('./flaskr.sqlite')
    # c = conn.cursor()
    # for row in c.execute('SELECT * FROM post'):
    #     print(row)
