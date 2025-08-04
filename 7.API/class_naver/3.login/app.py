from flask import Flask, render_template, redirect, request, url_for
from flask import session
from dotenv import load_dotenv
import sqlite3
import os
import requests


app = Flask(__name__)
app.secret_key = os.getenv('SESSION_SECRET')

PRAC_DATABASE = 'prac.db'

load_dotenv()

NAVER_CLIENT_ID = os.getenv('NAVER_CLIENT_ID')
NAVER_CLIENT_SECRET = os.getenv('NAVER_CLIENT_SECRET')
NAVER_REDIRECT_URI = os.getenv('NAVER_REDIRECT_URI')

def get_user(naverid):
    conn = sqlite3.connect(PRAC_DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM prac WHERE naverid=?", (naverid, ))
    user = cur.fetchone()
    conn.close()
    return user

def create_user(naverid, name, nickname, email, profile_image):
    conn = sqlite3.connect(PRAC_DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("INSERT INTO prac (naverid, name, nickname, email, profile_image) VALUES (?,?,?,?,?)", (naverid, name, nickname, email, profile_image))
    conn.commit()
    conn.close()

def extract_user_profile(profile):
    return {
        'naverid': profile.get('id'), 
        'name': profile.get('name'), 
        'nickname': profile.get('nickname'),
        'email': profile.get('email'),
        'profile_image': profile.get('profile_image')
    }

@app.route('/')
def index():
    user = session.get('user', None)
    print(user)
    return render_template('index.html', user=user)

@app.route('/login')
def login():
    # https://nid.naver.com/oauth2.0/authorize?client_id={클라이언트 아이디}&response_type=code&redirect_uri={개발자 센터에 등록한 콜백 URL(URL 인코딩)}&state={상태 토큰}
    auth_url = (
        f"https://nid.naver.com/oauth2.0/authorize?" +
        f"client_id={NAVER_CLIENT_ID}&response_type=code"
        f"&redirect_uri={NAVER_REDIRECT_URI}&state=xyz"
    )
    return redirect(auth_url)

@app.route('/naver/callback')
def naver_callback():
    code = request.args.get('code')
    state = request.args.get('state')

    # access_token 요청 / 받기
    # https://nid.naver.com/oauth2.0/token?client_id={클라이언트 아이디}&client_secret={클라이언트 시크릿}&grant_type=authorization_code&state={상태 토큰}&code={인증 코드}
    data = {
        'client_id': NAVER_CLIENT_ID,
        'client_secret': NAVER_CLIENT_SECRET,
        'grant_type': 'authorization_code',
        'code': code,
        'state': state
    }

    token_response = requests.post("https://nid.naver.com/oauth2.0/token", data=data).json()
    # print(token_response)
    access_token = token_response.get('access_token', None)
    # {'access_token': 'AAAAOtlwu3UtPfUkhkLAQle43hXgjVOfbsEI_4L9itiiW8JoyB4ZkAOOuMgzNEed1tYIN6Ad7oSTWq3jx1eoyy-KgIE', 'refresh_token': 'isisd6MEvuFwoii3nGEzOFO9GqRdbkRMeo2TkLGeLwDfA8OWdatvdj2lOip4FHEIlAGPCXADglKlfHYNoLXLNG9ZpX0qKsQ3YaC7sYAS4CT5pMJ1WHipLe1C9jXJii4NddypJR', 'token_type': 'bearer', 'expires_in': '3600'}

    
    # access_token 주면서 필요한 사용자 정보 요청 / 받기
    headers = {'Authorization': f"Bearer {access_token}"}
    profile = requests.post('https://openapi.naver.com/v1/nid/me', headers=headers).json()['response']
    # print(profile)
    info = extract_user_profile(profile)

    user = get_user(info.get('naverid'))

    if not user: 
        create_user(**info)
        user = get_user(info['naverid'])

    session['user'] = dict(user)
    
    return redirect(url_for('index'))


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)