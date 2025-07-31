# pip install flask_sqlalchemy
from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.secret_key = 'sesac' 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
# 객체 생성 전에 연결할 데이터베이스 설정 ( 경로 )
db = SQLAlchemy(app)
# 위의 설정을 기반한 연결 준비

app.config['SESSION_TYPE'] = 'sqlalchemy'
# 타입 지정
app.config['SESSION_SQLALCHEMY'] = db

Session(app)
# app에 세션 기능 더해주기


@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    session['count'] = 42
    session['my_list'] = ['apple', 'banana']
    session_store(session.sid, dict(session))

    return '세션이 저장되었습니다'

def session_store(sid, data):
    session_data = SessionData.query.get(sid)
    if not session_data:
        session_data = SessionData(id=sid)

    session_data.data = json.dumps(data)
    db.session.add(session_data)
    db.session.commit()

def get_session_data(sid):
    session_data = SessionData.query.get(sid)
    if session_data and session_data.data:
        return json.loads(session_data.data)
    return {}

@app.route('/get-session')
def get_session():
    stored_session_data = get_session_data(session.sid)
    stored_session_str = json.dumps(stored_session_data, indent=4)
    return f"저장된 정보: {stored_session_str}"

@app.route('/clear-session')
def del_session():
    session.pop('username', None) #세션에서 값 삭제
    return f"세션 정보를 삭제했습니다."

class SessionData(db.Model):
    id = db.Column(db.String(255), primary_key=True)
    data = db.Column(db.Text)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)