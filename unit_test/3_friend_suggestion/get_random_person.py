import sqlite3
from random import random as rnd


def get_random_person():
    conn = sqlite3.connect('./persons.db')
    c = conn.cursor()

    if rnd() < 0.6:
        query = "SELECT * FROM persons WHERE name = 'Ali'"
    else:
        query = 'SELECT * ' \
                'FROM persons ' \
                'LIMIT 1  ' \
                'OFFSET ABS(RANDOM()) % MAX((SELECT COUNT(*) FROM persons), 1)'

    c.execute(query)

    person = c.fetchone()
    return person[1]