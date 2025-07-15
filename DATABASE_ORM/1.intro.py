# pip install sqlalchemy

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db') #상대 경로로 설정 : 기본 디렉토리는 instance라는 폴더 만듦
# engine = create_engine('sqlite:////tmp/example.db') # 절대 경로 
# engine = create_engine('sqlite:///./example.db') #절대 경로  (현재 디렉토리에서)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine) #db에게 테이블 생성하라고 시키기

#세션: 실제 db와 crud하기
Session = sessionmaker(bind=engine)
sess = Session()

# INSERT INTO users VALUES ('Alice', 30)
new_user = User(name='Alice', age=30)
sess.add(new_user)
sess.commit()

users = sess.query(User).all()
# print(users)
for user in users:
    print(user.id, user.name, user.age)


