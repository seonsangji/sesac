import sqlite3

DATABASE = 'mycrm.db'

def get_connect():
    conn = sqlite3.connect(DATABASE)
    # 미션 1-1 : 여기 DB로부터 가져온 내용을 DICT로 하고 싶으면?
    # conn.row_factory = sqlite3.Row

    return conn

def get_stores():
    conn = get_connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM stores")
    stores = cur.fetchall()
    conn.close()
    # stores = [dict(r) for r in stores]
    # 미션 1-1을 하지 않았을 경우, 여기서 DICT로 변환 방법은?
    stores_dict = []
    for s in stores:
        stores_dict.append({
            'id': s[0],
            'name': s[1],
            'type': s[2],
            'address': s[3],
        })
    return stores




def get_stores_by_region(region):
    conn = get_connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM stores WHERE Name LIKE %", (( '%' + (region) + '%', )
    )
    stores = cur.fetchall()
    conn.close()

    stores = [dict(r) for r in stores]

    return stores