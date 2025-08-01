from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session

app = Flask(__name__)
app.secret_key = 'august-is-new-january'

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'BoB', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

@app.route('/', methods = ['GET', 'POST'])
def index():
    if session.get('user'):
        return redirect(url_for('welcome'))

    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        user = next((u for u in users if u['id'] == id and u['pw'] == password), None)
        if user:
            session['user'] = user
            flash("로그인 성공")
            return redirect(url_for('welcome'))
        else: 
            flash("ID 또는 비밀번호가 일치하지 않습니다")
            return render_template('index.html')
    return render_template('index.html')

@app.route('/dashboard')
def welcome():
    user = session.get('user')
    if user:
        flash("로그인 된 사용자이므로 대시보드를 실행합니다")
        return render_template('dashboard.html', name = user['name'])
    else:
        flash("대시보드를 확인하려면 로그인부터 하십시오.")
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("로그아웃하였습니다.")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)