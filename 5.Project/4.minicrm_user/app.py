from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():

    users = db.get_users_per_page(page, count)
    
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)