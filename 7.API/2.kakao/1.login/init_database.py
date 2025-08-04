import sqlite3

NAVER_DATABASE = 'kakao.db'

conn = sqlite3.connect(NAVER_DATABASE)

cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS ''')