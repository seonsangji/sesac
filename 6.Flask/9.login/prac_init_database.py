import sqlite3

MY_DATABASE = 'prac.db'

conn = sqlite3.connect(MY_DATABASE)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS prac
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    userid TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
            )
            ''')

conn.commit()
conn.close()





