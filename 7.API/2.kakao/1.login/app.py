from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for
from urllib.parse import urlencode
import requests
import os

load_dotenv()

app = Flask(__name__)

KAKAO_CLIENT_ID = os.getenv("KAKAO_REST_API_KEY")
KAKAO_CLIENT_SECRET = os.getenv("KAKAO_CLIENT_SECRET")
KAKAO_REDIRECT_URI = os.getenv("KAKAO_REDIRECT_URI")

def extract_user_profile(profile):
    properties = profile.get('properties')
    return {
        'kakao_id': profile['id'],
        'nickname': properties['nickname'],
        'profile_image': properties['profile_image']
    }


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    params = {
        'response_type' : 'code',
        'client_id' : KAKAO_CLIENT_ID,
        'redirect_uri' : KAKAO_REDIRECT_URI
    }
    kakao_auth_url = 'https://kauth.kakao.com/oauth/authorize?' + urlencode(params)
    return redirect(kakao_auth_url)

@app.route('/oauth/kakao/callback')
def callback():
    # print('RP에서 콜백 함수 실행')
    code = request.args.get('code')
    # print("코드값: ", code)

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    data = {
        'grant_type': 'authorization_code',
        'client_id': KAKAO_CLIENT_ID,
        'redirect_uri': KAKAO_REDIRECT_URI,
        'code': code,
        'client_secret': KAKAO_CLIENT_SECRET
    }

    token_response = requests.post("https://kauth.kakao.com/oauth/token", headers=headers, data=data).json()

    ACCESS_TOKEN = token_response.get('access_token')

    headers_for_profile = {
        'Authorization':  f'Bearer ${ACCESS_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    profile = requests.post("https://kapi.kakao.com/v2/user/me", headers=headers_for_profile).json()
    kakao_id = profile.get('id')



    # 성공 ? 사용자 정보 요청
    # 실패 ?
    # user_info = requests.get() # <--- 함수 파라미터에 위의 변수와 인자값들 채워넣기

    #로그인 성공
    # print(user_info)
    return "로그인 성공" # 어디로 보낼지 알아서 처리

@app.route('/profile')
def profile():
    # 사용자 정보 저장하고, 수정하기 기능 등 추가
    return render_template('profile.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)