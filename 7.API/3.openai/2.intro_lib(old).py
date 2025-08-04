import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = openai_api_key

# openai.ChatCompletion 문법을 사용 -> 구구구구버전, openai==0.3.0 이전 문법
response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': 'I want to make a project, making platform for pre-investment practice.'}
    ]
)

print(response['choices'][0]['message']['content'])