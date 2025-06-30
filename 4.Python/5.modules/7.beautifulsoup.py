# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup
# bs4라이브러리 안에 있는 특정 객체만 가져오기


response = requests.get("https://makemyproject.net")
print(response)
print(response.status_code)
print(response.text)
# 그냥 문자열


# html parsing
# 문자를 파싱한 , DOM  형태의 자료 구조
soup = BeautifulSoup(response.text, "html.parser")
print(soup)

head = soup.find("head")
print("헤드dom은:", head)

body = soup.find("body")

bodytext = body.text
print("바디내용은:",bodytext)