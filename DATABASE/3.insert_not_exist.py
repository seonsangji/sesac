import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()


cur.execute('''
            SELECT COUNT(*) FROM USERS
            ''')
count = cur.fetchone()[0]


if count == 0 :
    cur.execute('''
                INSERT INTO users(name,age) VALUES ('Sangji', 22)
                ''')
    cur.execute('''
                INSERT INTO users(name,age) VALUES (?,?)
                ''', ('Lunch', 0))
    cur.execute('''
                INSERT INTO users(name,age) VALUES (?,?)
                ''', ('Pongjja', 20))
    cur.execute('''
                INSERT INTO users(name,age) VALUES (?,?)
                ''', ('Rori', 18))

    
else:
    print('이미 데이터가 존재해서 더이상 삽입하지 않을 것임')
    print('현재 있는 사용자 데이터 갯수:', count)
#'?' 는 placeholder
# prepared statement.... SQL injection 공격을 막는 패턴


conn.commit()

conn.close()

