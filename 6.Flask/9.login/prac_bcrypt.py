from flask import Flask, render_template, request, redirect, url_for
from flask import session, flash
import sqlite3
import bcrypt

MY_DATABASE = 'prac.db'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sesac'

def get_user_by_id(userid):
    conn = sqlite3.connect(MY_DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM prac WHERE userid=? ''', (userid, ))
    user = cur.fetchone()
    conn.close()
    print(user)
    return dict(user)

def get_users(userid, password):
    
    user = get_user_by_id(userid)

    if user:
        hashed_pw = user['password']
        if bcrypt.checkpw(password.encode(), hashed_pw):
            return {
                'name': user['name'],
                'userid': user['userid'],
                'password': user['password']
                }
    return None


def create_user(name, userid, password):
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    conn = sqlite3.connect(MY_DATABASE)
    cur = conn.cursor()
    cur.execute("INSERT INTO prac (name, userid, password) VALUES (?,?,?)", (name, userid, hashed_pw))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        userid = request.form.get('userid')
        password = request.form.get('password')
        user = get_users(userid, password)
        if user:
            session['user'] = user
            flash("로그인 성공했습니다", 'success')
            return redirect(url_for('user'))
    flash("로그인 실패했습니다", 'danger')
    return redirect(url_for('index'))


@app.route('/user')
def user():
    user = session.get('user')
    return render_template('user.html', user=user)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST'])
def register():
    name = request.form.get('name')
    userid = request.form.get('userid')
    password = request.form.get('pw')
    confirm_password = request.form.get('confirm_pw') 

    if userid:
        existing_userid = get_user_by_id(userid)
        if existing_userid:
            flash("이미 사용 중인 id 입니다", "warning")
    if password == confirm_password:
        create_user(name=name, userid=userid, password=password)
        user = get_users(userid, password)
        print(user)
        session['user'] = user
        flash("회원가입 성공", "success")
        return redirect(url_for('user'))

    flash("회원가입 실패", "warning")
    return redirect(url_for('register_page'))


@app.route('/register', methods = ['GET'])
def register_page():
    return render_template('register.html')

    
    





if __name__ == '__main__':
    app.run(debug=True)