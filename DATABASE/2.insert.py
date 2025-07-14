import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
            INSERT INTO users(name,age) VALUES ('Sangji', 22)
            ''')

cur.execute('''
            INSERT INTO users(name,age) VALUES (?,?)
            ''', ('Pongjja', 20))
#'?' 는 placeholder
# prepared statement.... SQL injection 공격을 막는 패턴


conn.commit()

conn.close()

