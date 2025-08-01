from flask import Flask, render_template, request, redirect, url_for
from flask import session, flash
import sqlite3
import bcrypt

MY_DATABASE = 'prac.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sesac'

def get_users(username, password):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM users WHERE username=? AND password=?''', (username, hashed_pw))
    user = cur.fetchone()
    conn.close()
    return user


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user = get_users(username, password)
        if user:
            session['user'] = {'username':username, 'password':password}
            flash("로그인 성공했습니다", 'success')
            return redirect(url_for('user'))
        else:
            flash("로그인 실패했습니다", 'danger')
            return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/user')
def user():
    user = session.get('user')
    return render_template('user.html', name=user['name'])

if __name__ == '__main__':
    app.run(debug=True)