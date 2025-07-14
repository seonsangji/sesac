import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
            UPDATE users SET age=1 WHERE name='Lunch'
            ''')

cur.execute('''
            "UPDATE users SET age=? WHERE name=?", (0,'Lunch') )
            ''')

#'?' 는 placeholder
# prepared statement.... SQL injection 공격을 막는 패턴


conn.commit()

conn.close()

