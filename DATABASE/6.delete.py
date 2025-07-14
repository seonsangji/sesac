import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
            DELETE FROM users WHERE name='Lunch'
            ''')

cur.execute(
            'DELETE FROM users WHERE name=?', ('Sangji',)
            )

#'?' 는 placeholder
# prepared statement.... SQL injection 공격을 막는 패턴


conn.commit()

conn.close()

