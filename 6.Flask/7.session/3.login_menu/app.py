from flask import Flask, render_template, request, url_for, redirect
from flask import session

app = Flask(__name__)
app.secret_key = 'i-love-icecream-sooooo-much'

users = [
    {'name': 'sangji', 'id': 'ice', 'password': 'cream'}
]

items = [
    {'id': 'prod-001', 'name': 'strawberry', 'price':3900},
    {'id': 'prod-002', 'name': 'choco-mint', 'price':3900},
    {'id': 'prod-001', 'name': 'sangha-milk', 'price':2500},
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', name=user['name'])
    else:
        return '유저 없음'
        # return redirect(url_for('login'))
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form.get('id')
        password = request.form.get('password')
        user = next((u for u in users if u['id'] == id and u['password'] == password), None)
        if user:
            session['user'] = user # user 정보 모두 저장하기
            return redirect(url_for('user'))
        else:
            return render_template('login.html', error = 'ID 또는 비밀번호가 올바르지 않습니다.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop(user, None)
    return render_template('index.html')

@app.route('/product')
def add_to_cart():
    s_quantity = int(request.args.get('quantity1',0))
    c_quantity = int(request.args.get('quantity2',0))
    m_quantity = int(request.args.get('quantity3',0))
    price = 3900*s_quantity + 3900*c_quantity + 2500*m_quantity 
    # 버튼 눌리면 세션에 추가되기
    return render_template('product.html', price=price)

@app.route('/add_to_cart', methods=["POST"])
def add_to_cart():
    user = session.get('user')
    if not user:
        return render_template('product.html', user=None, items=items, error="로그인 후 사용할 수 있습니다")
    
    if "cart" not in session:
        session['cart'] = {}

    cart = session['cart'] #빈카트 또는 이전에 담은 카트

    if item_id in cart:
        cart[item_id] += 1
    else:
        cart[item_id] = 1

    session['cart'] = cart
    
    item_id = request.form.get('item_id')
    return f'got {item_id}!'



@app.route('/cart')
def view_cart():
    # 세션 목록을 보여줄 거다
    user = session.get('user')
    if not user:
            return render_template('product.html', user=None, items=items, error="로그인 후 사용할 수 있습니다")
    cart = session.get('cart', {})
    #카트가 없을 시 빈 딕셔너리 반환
    cart_items = []
    for item_id, item_qty in cart.items():
        item = next((i for i in items if i['id'] == item_id), None)
        if item:
            copied_item = item.copy()
            copied_item['qty'] = item_qty
    


if __name__ == '__main__':
    app.run(debug=True)