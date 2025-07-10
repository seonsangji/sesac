from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

users = [
    { "name": "Charlie", "id": "xcx", "pw": 3600 },
    { "name": "Clairo", "id": "o", "pw": 1234 },
    { "name": "Amine", "id": "vacation", "pw": 8282 },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':
        userID = request.form['ID']
        userPW = request.form['PW']
        # print(f"아이디: {userID}, 암호: {userPW}")

        user = None
        for u in users:
            if (u['id'] == userID) :
                if (u['pw'] == userPW):
                    user = u
                    break                   
                else:
                    return '비밀번호가 틀렸습니다.'
        if user is None:
            return "아이디없어용"
            
        return render_template('user.html', user=user)
        

    else:
        return render_template('login.html')
        
    
    
    #user=name))
        # return render_template('user.html', user=user)

    
@app.route('/user', methods=['GET'])    
@app.route('/user/<user>', methods=['GET'])
def user(user=None):
    return render_template('user.html', user=user)

@app.route('/product', methods=['GET'])
def product():
    return render_template('product.html')



if __name__ == '__main__':
    app.run(debug=True)