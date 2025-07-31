from flask import Flask, session

app = Flask(__name__)
app.secret_key = 'sesac' #세션 암호화를 위한 키 (외부 노출 xxx, 내가 관리, 암호화, 복호화 다아아아아)

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