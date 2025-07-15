import sqlite3

MY_DATABASE = 'users.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row
    #각각의 행이 tuple이 아닌 dict로 반환된다
    return conn

def create_table():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL)
    ''')

    conn.commit()
    conn.close()





def insert_user(name,age):
    conn = connect_db()
    cur = conn.cursor()

    # get_users()
    # count = cur.fetchone()[0]
    cur.execute(
        'INSERT INTO users(name,age) VALUES (?,?)', (name, age)
    )
    conn.commit()
    conn.close()

def get_users():
    conn = connect_db()
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()  

    conn.commit()
    conn.close()
    return dict(rows)

def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (name, ))
    rows = cur.fetchall()  

    conn.commit()
    conn.close()
    return dict(rows)

def get_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = ?", (id, ))
    user = cur.fetchone()
    conn.commit()
    conn.close()
    return dict(user)

def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))

    conn.commit()
    conn.close()

def update_user_by_id(id, new_name, new_age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("UPDATE users SET name=?,age=? WHERE name=?",(new_name, new_age, id))
    
    conn.commit()
    conn.close()
    

def delete_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE name=?", (name, ))

    conn.commit()
    conn.close()

def delete_user_by_age(age):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE age=?", (age, ))
    
    conn.commit()
    conn.close()

def delete_user_by_id(id):
    conn = connect_db()
    cur = conn.cursor()

    cur.execute("DELETE FROM users WHERE id=?", (id, ))
    
    conn.commit()
    conn.close()

