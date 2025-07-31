from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session
import json

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name': 'me', 'id': 'user', 'password': 'password'}
]

items = [
    {'id': 'prod-001', 'name': 'strawberry', 'price': 3900},
    {'id': 'prod-002', 'name': 'choco-mint', 'price': 3900},
    {'id': 'prod-003', 'name': 'shangha', 'price': 2500},
]

@app.route('/')
def home():
    user = session.get('users', None)
    if user:
        return render_template('user.html', user=user)
    else:
        return render_template('index.html')

@app.route('/logout')
def logout():
    session.pop('users', None)
    flash("로그아웃 되었습니다")
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET'])
def profile():
    user = session.get('users')
    print(user)
    return render_template('profile.html', user=user)

@app.route('/profile', methods=['POST'])
def change_profile():
    new_name = request.form.get('name')
    new_id = request.form.get('id')
    new_password = request.form.get('password')
    user = session.get('users')
    user['name'] = new_name
    user['id'] = new_id
    user['password'] = new_password
    session['users'] = user
    print(user)
    flash("사용자가 개명하였습니다")
    return redirect(url_for('profile'))

@app.route('/login', methods = ['POST'])
def login():
    id = request.form.get('id')
    password = request.form.get('password')
    user = next((u for u in users if u['id'] == id and u['password'] == password), None)
    if user:
        session['users'] = user
        return render_template('user.html', user=user)
    return render_template('login.html', error='로그인에 실패하였습니다.')
    
@app.route('/login', methods = ['GET'])
def login_index():
    return render_template('login.html')

@app.route('/product', methods = ['GET'])
def product():
    return render_template('product.html', items=items)

@app.route('/product', methods = ['POST'])
def add_to_cart():
    
    item = json.loads(request.form.get('item_json'))
    
    cart = session.get('cart', [])

    for i in cart:
        if i['id'] == item['id']:
            i['qty'] += 1
            break
    else:
        item['qty'] = 1
        cart.append(item)
        
    session['cart'] = cart
    print(cart)
    return redirect(url_for('product'))

@app.route('/cart')
def cart():
    user = session.get('user')
    if user:
        cart = session.get('cart', [])
        return render_template('cart.html', cart=cart)
    else:
        flash("장바구니를 확인하려면 로그인부터 해야합니다.")
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)