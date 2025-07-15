from flask import Flask, render_template, request, redirect


app = Flask(__name__)

users=[]
next_id = 1



@app.route('/', methods=['GET', 'POST'])
def index():
    global next_id
    
    if request.method == 'POST':

        name = request.form['name']
        age = int(request.form['age'])
    
        users.append({'id': next_id, 'name': name, 'age': age})
        next_id += 1
        return redirect('/')
    
    print('index의 전체 사용자: ', users)    
    return render_template('index.html', users = users)

@app.route('/delete/<int: user_id>')
def delete_user(user_id):
    for i,u in enumerate(users):
        if u['id'] == user_id :
            del users[i]
            break
    return redirect('/')
    


if __name__ == '__main__':
    app.run(debug=True)
