#pip install flask-sqlalchemy
from flask import Flask, request, redirect, render_template
from models import db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db.init_app(app) #여기서 초기화


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users = users)

@app.route('/add')
def add_user(name, age):
    name = request.form.get('name')
    age = int(request.form.get('age'))

    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/') # redirect(url_for('index')) 가 더 나은 코드

@app.route('/delete/<int: user_id>')
def delete_user(user_id):
    user = db.session.get(User, user_id) 
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print("사용자 없음: ", user_id)

    return redirect('/')

@app.route('/edit/<int: user_id>', methods = ['GET', 'POST'] )
def update_user(user_id):
    user = db.session.get(User, user_id)

    if not user:
        return "사용자를 찾을 수 없습니다", 404
    
    if request.method == 'POST':
    
        new_name = request.form.get('name')
        new_age = int(request.form.get('age'))
        user.name = new_name
        user.age = new_age
        
        db.session.commit()
        return redirect('/')



if __name__ == '__main__':
    # app = create_app()
    app.run(debug=True)




