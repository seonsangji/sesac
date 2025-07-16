from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def index():
    query = request.args.get('q')

    page = request.args.get('page', default = 1, type= int)

    print(query, page)

    return "Hello"



if __name__ == '__main__':
    app.run(debug=True)