from flask import Flask, request, render_template

app = Flask(__name__)

users = [
{'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
{'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
{'name': 'Bob', 'age': 35, 'mobile': '050-4444-5678'},
{'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'}
]


# for i in range(len(users[0].keys())):


@app.route('/')
def home():
    name = request.args.get("name", default= None)
    age = request.args.get("age", default= None)
    mobile = request.args.get("mobile", default= None)
    # print(f"이름: {name}, 나이: {age}, 번호: {phone}")


    if name is None and age is None and mobile is None:
        filtered_users = []
    else:
        filtered_users = []
        for user in users:
            if (
                (user['name'].lower() == name.lower() or name is None) and
                (age is None or user['age'] == int(age)) and
                ( mobile in user['mobile']  or mobile is None)
            ):
                filtered_users.append(user)

# count_list[0]부터 비교
#  이름 매칭되거나 none 이다 -> age 매칭되거나 none 이다 -> mobile 매칭이거나 mobile none 인거 고르기/ mobile 매칭 안된다면 안고르기

# 뭐든 매칭되거나 none 이면 고르자!

            




    return render_template('index5.html', users= filtered_users)


if __name__ == "__main__":
    app.run(debug= True, port= 5000)
