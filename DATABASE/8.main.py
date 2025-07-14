from db_crud_sqlite import (
    create_table, 
    insert_user, 
    get_users, 
    update_user_age, 
    get_user_by_name, 
    delete_user_by_name, 
    delete_user_by_age)


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