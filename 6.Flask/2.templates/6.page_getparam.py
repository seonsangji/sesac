from flask import Flask, render_template, request

app = Flask(__name__)

# 더미 유저 100명 생성
users = [
    { 'id': i, 'name': f'User{i}', 'age': 20 + i % 10, 'phone': f'010-0000-{str(i).zfill(4)}' } for i in range(1, 101)
]

# http://localhost:5000/?pages=1
@app.route('/')
def index():
    page = request.args.get('pages', default= "1")
    page_num = int(page)
    for _ in range(1, 11):
        page_users = []
        for user in [u for u in users if u['id'] // 10 == (page_num -1)] :
            page_users.append(user)        
    return render_template('users.html', users=page_users, page=page_num)

if __name__ == "__main__":
    app.run(debug=True)