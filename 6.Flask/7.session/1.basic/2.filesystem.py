# pip install flask-session
from flask import Flask, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = 'sesac' 

app.config['SESSION_TYPE'] = 'filesystem'
# 기본 값이 null : 서버에 저장하지 않는다.
# 그 외에 filesystem , redis, memchanced, mongod, sqlalchemy 등등에 저장 가능
app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(), 'my_sessions')
# 이제 저장할 파일 경로 설정해주자

app.config['SESSION_PERMANENET'] = False
# False : 브라우즈가 닫히면 삭제하라
app.config['SESSION_USE_SIGNER'] = True
# True : 세션 쿠키에 서명 사용 하겠다


Session(app)
# app에 세션 기능 더해주기

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션이 저장되었습니다'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f"세션정보: {session['username']}"
    else:
        return f"저장된 정보가 없습니다."

@app.route('/clear-session')
def del_session():
    session.pop('username', None) #세션에서 값 삭제
    return f"세션 정보를 삭제했습니다."


if __name__ == "__main__":
    app.run(debug=True)