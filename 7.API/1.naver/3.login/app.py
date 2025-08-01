from flask import Flask, render_template, redirect, request, session, url_for
from dotenv import load_dotenv
import os
import requests #내가(새싹이) 다른 사람(네이버) 한테 요청할 때 사용

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

NAVER_CLIENT_ID = os.getenv("NAVER_CLIENT_ID")
NAVER_CLIENT_SECRET = os.getenv("NAVER_CLIENT_SECRET")
NAVER_REDIRECT_URI = os.getenv("NAVER_REDIRECT_URI")

@app.route('/')
def index():
    user = session.get('user', None)
    return render_template('index.html', user=user)

@app.route('/login/naver/')
def login_naver():
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?"
        f"response_type=code&client_id={NAVER_CLIENT_ID}"
        f"&redirect_uri={NAVER_REDIRECT_URI}&state=xyz"
    )
    return redirect(auth_url)

@app.route('/naver/callback')
def naver_callback():
    code = request.args.get('code') # 서버가 인증 성공의 댓가로 준 값
    state = request.args.get('state') # 내 사이트에서 갔다 온건지 확인용...
    print(f"code: {code}, state: {state}")
    # 내가 네이버와 앞으로 대화하기 위한 인증 토큰 요청 ( code 검증 이후 맞으면 서버는 토큰을 줌 )
    token_url = (
        f"https://nid.naver.com/oauth2.0/token?"
        f"grant_type=authorization_code&client_id={NAVER_CLIENT_ID}"
        f"&client_secret={NAVER_CLIENT_SECRET}&code={code}&state={state}"
    )
    token_response = requests.get(token_url).json()
    print(token_response)
    access_token = token_response.get('access_token')
    # 사용자의 인증 확인, naver에게 해당 사용자 정보 요청

    headers = {"Authorization": f"Bearer {access_token}"}
    profile = requests.get('https://openapi.naver.com/v1/nid/me', headers=headers).json()

    print('최종적으로 받아온 사용자 정보:', profile)   

    # (숙제): 나의 db에 이 사용자가 있는지 확인하고, 있으면 그 정보 가져와 세션에 저장
    # db에 사용자 없으면? -> 새롭게 db에 삽입 OR 회원가입시키기

    # 해당 정보를 내 세션에 저장하기 
    session['user'] = profile['response']

    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.clear() # 해당 사용자의 세션 모두 제거
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
