from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'yummm'

users = [
    {'name':'aa', 'id': 'user', 'pw': 'password'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == 'POST':
        user = request.form.get('id')
        password = request.form.get('password')
        user = next((u for u in users if u['id'] == user and u['pw'] == password), None)
        if user:
            session['user'] = user
            flash("로그인에 성공했습니다")
            return redirect(url_for('user'))
        flash("ID 또는 PW 가 일치하지 않습니다")
        return redirect(url_for('home'))
    if 'user' in session:
        return redirect(url_for('user'))
    return redirect(url_for('home'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session.get('user')
        flash("이미 로그인 된 사용자입니다")
        return render_template('dashboard.html', name=user['name'])
    
    flash("로그인부터 하세요 ㅡㅡ")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("정상적으로 로그아웃 되었습니다")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)