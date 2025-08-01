import urllib.request
import json

client_id = ''
client_secret = ''
text = "Python programming"

enrText = urllib.parse.quote(text)
url = 'https://openapi.naver.com/v1/search/blog?query='+enrText

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()
if rescode == 200:
    response_body = response.read()
    print(response_body.decode('utf-8'))
