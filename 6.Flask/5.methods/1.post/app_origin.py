from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['ID']
        print("아이디: ", user)
        return redirect(url_for("user", user=user))
        # return render_template('user.html', user=user)

    else:
        return render_template('login.html')
    
@app.route('/product', methods=['GET'])
def product():
    return render_template('product.html')

@app.route('/user', methods=['GET'])    
@app.route('/user/<user>', methods=['GET'])
def user(user=None):
    return render_template('user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)