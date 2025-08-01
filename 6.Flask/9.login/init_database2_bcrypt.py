import sqlite3
import bcrypt

DB_FILENAME = 'users.db'

conn = sqlite3.connect(DB_FILENAME)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            name TEXT NOT NULL)
''')

def create_user(username,password,name):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrpyt.gensalt())
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (username, password, name) VALUES (?,?,?)", (username, hashed_pw, name))
    conn.commit()
    conn.close()
    
create_user(,,)
create_user(,,)