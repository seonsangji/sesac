from flask import Flask, render_template

app = Flask(__name__)

users = [
    { 'id': i, 'name': f'User{i}', 'age': 20+ i % 10, 'phone': f'010-0000-{str(i).zfill(4)}'} for i in range (1, 101)
]

@app.route('/')
def index():
    return render_template('users.html', users=users)


@app.route('/pages/<int:num>')
def pages(num):
    for _ in range(1, 11):
        page_users = []
        for user in [u for u in users if u['id'] // 10 == (num -1)] :
            page_users.append(user)        
    # return page_users

    return render_template('users.html', users=page_users)



if __name__ == '__main__':
    app.run(debug= True, port= 5000)