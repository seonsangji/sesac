import sqlite3

PRAC_DATABASE = 'prac.db'

conn = sqlite3.connect(PRAC_DATABASE)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS prac (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            naverid TEXT NOT NULL,
            name TEXT NOT NULL,
            nickname TEXT NOT NULL,
            email TEXT NOT NULL,
            profile_image TEXT
            )
            ''')

conn.commit()
conn.close()