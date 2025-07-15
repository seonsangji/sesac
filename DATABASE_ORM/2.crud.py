from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///users.db')

Base = declarative_base()

class User(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
sess = Session()


#CRUD 만들기
def create_user(session, name:str, age:int) -> User:
    new_user = User(name=name, age=age)
    sess.add(new_user)
    sess.commit()
    return new_user


def get_users(session)-> list[User]:
    #아무 인자도 안 받아서, 사용자 리스트 리턴하기
    return sess.query(User).all()
    

def get_user_by_id(session, user_id: int) -> User | None:
    #사용자 ID를 받아서 사용자 반환하기 ( 사용자 없을 수도 있다 - 빈거 그냥 return )
    user = sess.get(User, user_id) #SQLAlchemy 2.x부터 등장
    # user = session.query(User).filter_by(user_id).first()
    return user

def update_user_age(session, user_id: int, new_age: int) -> bool:
    #사용자 아이디와 나이를 받아서, 나이 업데이트 하기
    #객체에 값만 설정하면 , 자동으로 쓰인다 (물론 sess.commit() 은 해야한다)
    user = sess.get(User, user_id)
    if not user:
        return False
    user.age = new_age
    session.commit()
    return True

def delete_user_by_id(session, user_id: int) -> bool:
    #사용자를 삭제하고 성공시 True 리턴
    user = sess.get(User, user_id)
    if not user:
        return False
    sess.delete(user)
    sess.commit()
    return True

def delete_user_by_name(session, name: int) -> bool:
    #사용자를 삭제하고 성공시 삭제 한 사용자 수 리턴
    user = sess.query(User).filter_by(name=name).all
    if not user:
        return 0
    for u in users:
        sess.delete(u)
    sess.commit()
    return len(users)

if __name__ == "__main__":
    Session = sessionmaker(bind=engine, expire_on_commit=False)
    with Session() as sess:
        # 1) 사용자 생성
        alice = create_user(sess, 'Alice', 30)
        bob = create_user(sess, 'Bob', 40)
        print(f"추가된 사용자 id: {alice.id}, {bob.id}")

        # 2) 사용자 조회
        user1 = get_user_by_id(sess, alice.id)
        print(f"조회한 사용자 정보: {user1.name, user1.age}")

        user2 = get_user_by_id(sess, bob.id)
        print(f"조회한 사용자 정보: {user2.name, user2.age}")

        # 3) 정보 수정
        update_alice = update_user_age(sess, alice.id, 29)
        print(f"업데이트 성공 실패 여부 확인: ", update_alice)

        # 4) 사용자 모두 조회
        users = get_users(sess)
        for u in users:
            print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}")

        # 5) 사용자 삭제
        delete_alice = delete_user_by_id(sess, alice.id)
        print(f"Alice 삭제 성공 실패 여부: ", delete_alice)

        del_user_count = delete_user_by_name(sess, 'Bob')
        print(f"Bob이라는 사용자를 모두 삭제한 개수: ", del_user_count)

        # 6) 최종 사용자 목록
        users = get_users(sess)
        for u in users:
            print(f"ID: {u.id}, Name: {u.name}, Age: {u.age}")