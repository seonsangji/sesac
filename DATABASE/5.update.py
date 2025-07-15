import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute(
        'UPDATE users SET age = ? WHERE name = ?', (40, 'Alice')
            )

conn.commit()

conn.close()
