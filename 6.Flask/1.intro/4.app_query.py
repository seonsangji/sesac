from flask import Flask, request

app = Flask(__name__)

@app.route('/search') 
    #  "127.0   /search?q=apple&page=2"

def search():
    query = request.args.get('q')
    page = request.args.get('page', default=1, type=int)
    print(query, page)
    return "hello"

if __name__ == "__main__":
    app.run(debug= True)

