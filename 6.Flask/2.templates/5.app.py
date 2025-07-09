from flask import Flask, render_template, request

app = Flask(__name__)

users_dic = [
{'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
{'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
{'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'}
]

# get 파라미터 요청도 같이 온다
@app.route('/')
def home():
    name = request.args.get('name')
    age = request.args.get('age')
    print(f"이름:{name}, 나이:{age}")
    filtered_users = users_dic

    # if name:
    #     filtered_users = [u for u in users_dic if u['name'].lower() == name.lower()]

    # print(filtered_users)
    return render_template('index5.html', users = filtered_users, age = age)

if __name__ == '__main__':
    app.run(debug=True)