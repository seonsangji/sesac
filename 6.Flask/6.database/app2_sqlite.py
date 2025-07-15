from flask import Flask, render_template, request, redirect
import database as db

app = Flask(__name__)
db.create_table()


@app.route('/', methods=['GET', 'POST'])
def index():

    #글로벌 변수 write를 할 때 필요 (read 시에는 필요 없다)
    if request.method =='POST':
        
        name = request.form['name']
        age = int(request.form['age'])
        db.insert_user(name, age)
        return redirect('/')
    users = db.get_users() #dict로 변환 가능한 row로 왔다..

    return render_template('index.html', users = users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):  
    # 미션1: users 라는 변수를 뒤져서, user_id 를 찾아서, 지운다

    db.delete_user_by_id(user_id)
    # print(users)
    return redirect('/')

@app.route('/update/<int:user_id>', methods = ['GET', 'POST'])
def update_user(user_id):
    if not user: 
        return "사용자를 찾을 수 없습니다.", 404
    

    if request.method == 'POST':
        user = db.get_user_by_id(user_id)

        name = request.form['name']
        age = int(request.form['age'])

        db.update_user_by_id(user_id, name,age)
        return redirect('/')
    
    user = next((u for u in users if u['id'] == user_id), None)
    print(user)


    return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)