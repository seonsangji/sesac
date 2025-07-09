from flask import Flask, request

app = Flask(__name__)

@app.route('/') 


def home():
    return """
<h1>Hello, Flask!</h>
<h2>안녕하세여</h2>
<p>상품목록</p>
    <div>
        <ul>
            <li>아메리카노</li>
            <li>카푸치노</li>
        </ul>
    </div>
    """
if __name__ == "__main__":
    app.run(debug= True)

