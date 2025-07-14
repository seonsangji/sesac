import sqlite3

MY_DATABASE = 'example.db'

def connect_db():
    conn = sqlite3.connect(MY_DATABASE)
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
    return rows

def get_user_by_name(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = ?", (name, ))
    rows = cur.fetchall()  

    conn.commit()
    conn.close()
    return rows


def update_user_age(name, new_age):
    conn = connect_db()
    cur = conn.cursor()


    cur.execute("UPDATE users SET age=? WHERE name=?", (new_age, name))

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



def main():

    create_table()

    insert_user('Sangji', 22)
    insert_user('Pongjja', 20)
    insert_user('Mom', 53)

    print("데이터 목록:")

    users = get_users()
    for user in users:
        print(user)

    update_user_age('Pongjja', 21)

    user = get_user_by_name('Pongjja')
    print(user)

    delete_user_by_name('Mom')
    print("사용자 조회:")
    user = get_user_by_name('Mom')
    print(user)

    print("데이터 목록:")
    users = get_users()
    for user in users:
        print(user)

    delete_user_by_age(22)
    
    print("데이터 삭제 후:")
    users = get_users()
    for user in users:
        print(user)

if __name__ =='__main__':
    main()