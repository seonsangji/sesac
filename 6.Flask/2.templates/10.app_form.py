from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    #post로 form이 전달된 것 안에서 name이 키인 것을 주시오.
    age = request.form.get('age')

    # print(request.form)
    return f'Hello, {name}! You must be {age} :( '

if __name__ == '__main__':
    app.run(debug= True)

