import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

client = openai.OpenAI(api_key=openai_api_key)

# client.chat.completion -> 0.3 이후 버전
response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {'role': 'user', 'content': 'I want to make a project, making platform for pre-investment practice, targeting for a personal, unprofessional individual'}
    ]
)

print(response.choices[0].message.content)