import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute(
    'DELETE FROM users WHERE id =?', (7,)
)


conn.commit()

conn.close()