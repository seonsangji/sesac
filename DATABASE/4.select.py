import sqlite3

conn = sqlite3.connect('example.db')

cur = conn.cursor()

cur.execute('''
            SELECT * FROM users
            ''')

# 결과 가져오기: 모든 행 다 가져오기 fetchall()

rows = cur.fetchall()
print(rows)

for row in rows:
    print(row)
#'?' 는 placeholder
# prepared statement.... SQL injection 공격을 막는 패턴

cur.execute('''
            SELECT * FROM users
            ''')
print("-----------------")
rows = cur.fetchone()
print(rows)


print("-----------------")
cur.execute('''
            SELECT COUNT(*) FROM users
            ''')
rows = cur.fetchone()[0]
print(rows)

conn.commit()

conn.close()

