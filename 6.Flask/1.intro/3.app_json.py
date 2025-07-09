from flask import Flask, jsonify


app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'}
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_user_by_name(name):

    user = None
    for i in range(len(users)):
        print(i)        
        if name.lower() == users[i]['name'].lower():
            user = users[i]
            break                
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User Not Found'}), 404
    
@app.route('/user/<int:age>')
def get_user_by_age(age):

    user = None
    for i in range(len(users)):
        print(i)        
        if age == users[i]['age']:
            user = users[i]
            break                
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User Not Found'}), 404



if __name__ == "__main__":
    app.run(debug=True, port= 5000)


