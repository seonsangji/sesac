from flask import Flask, jsonify

users = [
{'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
{'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
{'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'}
]

def get_user(input):
    user = None

    user = None
    for i in range(len(users)):
        print(i)        
        if input.lower() == users[i]['name'].lower():
            user = users[i]
            break               

    for i in range(len(users)):
        if input == str(user['age']):
            user = users[i]
            break

    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User Not Found'}), 404
