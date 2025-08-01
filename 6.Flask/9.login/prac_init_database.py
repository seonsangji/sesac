import sqlite3
import bcrypt

MY_DATABASE = 'prac.py'

conn = sqlite3.connect(MY_DATABASE)
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXIST users
    id INTEGER PRIMARY KEY AUTOINCREMENT
    username TEXT UNIQUE NOT NULL
    password TEXT NOT NULL
    name TEXT NOT NULL
            ''')

def create_user(username, password, name):
    salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password.encode(), salt)
    conn = sqlite3.connect()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (username, password, name) VALUES (?,?,?)', (username, hashed_pw, name))
    conn.commit()
    conn.close()

create_user('username1', 'password1', 'name1')
create_user('username2', 'password2', 'name2')


