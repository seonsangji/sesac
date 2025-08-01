import requests
import json
from dotenv import load_dotenv
import os
from tabulate import tabulate

load_dotenv()

client_id = os.getenv("NAVER_CLIENT_ID")
client_secret = os.getenv("NAVER_CLIENT_SECRET")
text = "TIGER 200"

encText = requests.utils.quote(text)
url = 'https://openapi.naver.com/v1/search/news?query='+encText

headers = {
    "X-Naver-Client-Id" : client_id,
    "X-Naver-Client-Secret": client_secret
}

response = requests.get(url, headers = headers)
if response.status_code == 200:
    response_body = response.text
    
    data = json.loads(response_body)

    selected_columns = [['title', 'link', 'description']]
    for item in data["items"]:
        # print(item['title'], item['link'])
        selected_columns.append([item['title'], item['link'], item['description']])

    print(tabulate(selected_columns, headers="firstrow", tablefmt="list"))