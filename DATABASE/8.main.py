import db_crud_sqlite as db



def main():

    db.create_table()

    db.insert_user('Sangji', 22)
    db.insert_user('Rori', 18)
    db.insert_user('Pongjja', 20)

    data = db.get_users()
    print("데이터 목록: ")
    for user in data:
        print(user)

    print("--------")
    db.update_user_by_id(10, 'Daeun', 22)
    data = db.get_users()
    print("수정 후 데이터 목록: ")
    for user in data:
        print(user)

    print("--------")
    db.delete_user_by_id(10)

    db.delete_user_by_age(40)
    
    db.delete_user_by_name('Rori')











    print("사용자 삭제 후 데이터 목록: ")
    data = db.get_users()
    print("삭제 후 데이터 목록:")
    for _ in data:
        print(_)


if __name__ == '__main__':
    main()