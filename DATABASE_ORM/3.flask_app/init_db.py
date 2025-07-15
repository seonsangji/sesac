from app import app
from models import db, User

app = create_app()

with app.app_context(): #위의 flask app 이 초기화되면 -> db 만들자

    db.drop_all() #모든 테이블 삭제
    db.create_all() # 새로 초기화

    db.session.add(User(name='Sangji', age=22))
    db.session.add(User(name='Pongjja', age=21))
    db.session.add(User(name='Rori', age=18))
    db.session.commit()

    for u in User.query.all():
        print(u.id, u.name, u.age)

