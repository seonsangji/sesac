import sqlite3

MY_DATABASE = 'example.db'

def connect():
    conn = sqlite3.connect(MY_DATABASE)
    return conn

def create_table():
    conn = connect()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
                )''')
    
    conn.commit()
    conn.close()

def insert_user(name, age):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO users (name, age)  VALUES (?, ?)", (name, age))
    
    conn.commit()
    conn.close()

def get_users():
    conn = connect()
    cur = conn.cursor()

    cur.execute('''SELECT * FROM users''')
    rows = cur.fetchall()

    conn.commit()
    conn.close()
    return rows

def get_user_by_name(name):
    conn= connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE name=?", (name, )
    )
    user = cur.fetchone()

    conn.commit()
    conn.close()
    return user

def get_user_by_age(age):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        'SELECT * FROM users WHERE age=?', (age,)
    )
    user = cur.fetchone()

    conn.commit()
    conn.close()

    return user

def update_age_by_name(name,new_age):
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        'UPDATE users SET age=? WHERE name = ?', (new_age, name)
    )
    conn.commit()
    conn.close()

def update_user_by_id (user_id, name, age):

    conn= connect()
    cur = conn.cursor()

    cur.execute(
        'UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id)
    )
    conn.commit()
    conn.close()

def delete_user_by_name(name):
    conn= connect()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM users WHERE name = ?', (name,)
    )
    conn.commit()
    conn.close()

def delete_user_by_age(age):
    conn= connect()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM users WHERE age = ?', (age,)
    )
    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn= connect()
    cur = conn.cursor()

    cur.execute(
        'DELETE FROM users WHERE id = ?', (id,)
    )
    conn.commit()
    conn.close()
    