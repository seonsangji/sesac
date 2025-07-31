from flask import Flask, request, render_template

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'mobile': '050-1234-5678'},
    {'name': 'Bob', 'age': 30, 'mobile': '050-2222-5678'},
    {'name': 'Charlie', 'age': 35, 'mobile': '050-3333-5678'},
]

@app.route('/')
def home():
    name = request.args.get('name')
    
    # filtered_users = users

    # for u in users:
    #     if name.lower() == u['name'].lower():
    #         filtered_users = [u]
    #         break
    filtered_users = users
     
    if name :
        filtered_users = [u for u in users if u['name'].lower() == name.lower()]

    return render_template('index4.html', users = filtered_users)

if __name__ == '__main__':
    app.run(debug=True)