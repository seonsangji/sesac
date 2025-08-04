# pip install flask-mail
from flask import Flask, request, jsonify, render_template, session, redirect, url_for
from flask_mail import Mail, Message
import random

import os
from dotenv import load_dotenv
load_dotenv()

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
NAVER_EMAIL = os.getenv("NAVER_EMAIL")
NAVER_PASSWORD = os.getenv("NAVER_PASSWORD")


app = Flask(__name__)
app.secret_key = "sesac"

app.config["MAIL_SERVER"] = os.getenv("SMTP_SERVER")
app.config["MAIL_PORT"] = os.getenv("SMTP_PORT")
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("NAVER_EMAIL")
app.config["MAIL_PASSWORD"] = os.getenv("NAVER_PASSWORD")
mail = Mail(app)


@app.route('/')
def signup():
    email = session.get('email')
    return render_template('index.html', email=email)

@app.route('/send-code', methods=['POST'])
def send_code():
    email = request.form.get('email')
    code = str(random.randint(0,999999)).zfill(6)

    session['user'] = {
        'email': email,
        'code': code
    }
    # result = send_code_by_email()
    # 사용자 이메일로 코드 보내기...
    msg = Message("회원가입 인증 코드", sender=app.config['MAIL_USERNAME'], recipients=[email])

    msg.body = f"인증 코드: {code}"

    mail.send(msg)

    return redirect(url_for('signup'))

    # if result: 

    
    # 세션에 이메일, 코드 저장
    # 저장된 세션으로부터 코드 가져와서 사용자 입력값과 나의 저장 세션값 같은지 확인
    



@app.route('/verify-code', methods=['POST'])
def verify_code():
    user_code = request.form.get('user_code')
    code = session.get('code')
    if code == user_code:
        return jsonify({"message": "인증 성공 !"})
    else:
        return jsonify({"message": "인증 실패"})
    

if __name__ == '__main__':
    app.run(debug=True)