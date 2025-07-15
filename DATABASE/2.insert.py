import sqlite3

def insert_user(name,age):

    conn = sqlite3.connect('example.db')

    cur = conn.cursor()
  
    cur.execute("INSERT INTO users ( name, age ) VALUES ( ? , ?)", (name, age))


    conn.commit()

    conn.close()



