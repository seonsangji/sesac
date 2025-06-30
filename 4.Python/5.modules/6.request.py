# pip install requests
# pip uninstall requests

import requests

requests.get("https://makemyproject.net")

response = requests.get("https://makemyproject.net")
print(response)
print(response.status_code)
print(response.text)