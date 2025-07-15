import sqlite3


conn= sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('SELECT * FROM users')
rows = cur.fetchall()
print(rows)

print('------------------')

cur.execute('SELECT COUNT(*) FROM users')
row = cur.fetchone()[0]
print(row)

conn.commit()

conn.close()