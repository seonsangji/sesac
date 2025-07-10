from flask import Flask, send_file, jsonify

app = Flask(__name__)

@app.route('/')
def  index():
    return send_file("4.fetch.html")

@app.route('/data')
def data():
    return jsonify({'result':'success', 'messagae': 'Salut! !' })

if __name__ == '__main__':
    app.run(debug=True)