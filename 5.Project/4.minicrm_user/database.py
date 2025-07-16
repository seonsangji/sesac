import sqlite3

DATABASE = 'mycrm.db'

def get_connect():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_users():
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    data = cur.fetchall()
    users = [dict(r) for r in data]
    print("get_user함수를 통해 select 한 것 : ", users)
    conn.commit()
    conn.close()
    return users

def get_users_per_page(page, count):
    offset = (page-1) * count
    conn = get_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users LIMIT ? OFFSET ?', (count, offset))
    data = cur.fetchall()
    users = [dict(r) for r in data]
    print("get_user함수를 통해 select 한 것 : ", users)
    conn.commit()
    conn.close()
    return users

