from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    users_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
    return render_template("index2.html", users = users_list)
# 이때 이 파일은 무조건 templates 폴더 안에 있어야 한다!!
# HTML 팡리 안데 users 라는 키에 users_list 값을 담을 것이다
if __name__ == '__main__':
    app.run(debug=True)