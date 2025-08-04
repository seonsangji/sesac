from dotenv import load_dotenv
from flask import Flask, request, render_template, session, redirect, url_for, flash
from urllib.parse import urlencode
import requests
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SESSION_SECRET')

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
    user = session.get('user', None)
    return render_template('index.html', user=user)

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
    code = request.args.get('code')
    if not code:
        return "인가 코드가 없습니다", 400
    
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

    # code 확인을 통해 access_token 요청 
    token_response = requests.post("https://kauth.kakao.com/oauth/token", headers=headers, data=data).json()

    # access_token 받기
    ACCESS_TOKEN = token_response.get('access_token')

    headers_for_profile = {
        'Authorization':  f'Bearer ${ACCESS_TOKEN}',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8'
    }

    profile = requests.post("https://kapi.kakao.com/v2/user/me", headers=headers_for_profile).json()
    # kakao_id = profile.get('id')
    # print('kakao_id')
    user = extract_user_profile(profile)
    session['user'] = user
    
    # kakao_id = user['kakao_id']
    # if kakao_id:
    #     session['user'] = profile
    #     flash("로그인 성공", "success")

    # 성공 ? 사용자 정보 요청
    # 실패 ?
    # user_info = requests.get() # <--- 함수 파라미터에 위의 변수와 인자값들 채워넣기

    #로그인 성공
    # print(user_info)
    return redirect(url_for('profile')) # 어디로 보낼지 알아서 처리

@app.route('/profile')
def profile():
    user = session.get('user')
    if not user:
        return redirect(url_for('login'))
    # 사용자 정보 저장하고, 수정하기 기능 등 추가
    return render_template('profile.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)