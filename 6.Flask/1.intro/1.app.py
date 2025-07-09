from flask import Flask

app = Flask(__name__)
app2 = Flask(__name__)
app3 = Flask(__name__)

@app.route('/') #사용자가 /에 접속하면, 이 아래 함수를 호출해줘
def home():
    return "<h1>Hello, Flask!</h1>"


@app.route('/user') #사용자가 /에 접속하면, 이 아래 함수를 호출해줘
def user():
    return "<h1>Hello, User!</h1>"

@app.route('/user/<username>') 
def username(username):
    print(username)
    return f"<h1>Hello, {username}!</h1>"

@app.route('/user/<int:age>') 
def userage(age):
    print(age)
    return f"<h1>Hello, your age is {age}!</h1>"


@app.route('/product') 
def product():
    return "<h1>Hello, Product!</h1>"


# 비지니스 로직


@app.route('/user/<name>/<int:age>/<float:weight>')
def greet_user_with_detail(name, age, weight):
    return f"<h1>안녕하세요</h1><h2>사용자정보</h2><ul><li>이름:{name}</li><li>이름:{age}</li><li>이름:{weight}</li>"

if __name__ == '__main__':
    print("이게 메인 함수")
    # app.run(debug= True) 
    # 절대루 이대로 커밋해선 안된다 ~~

