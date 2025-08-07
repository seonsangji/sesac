import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

history = []

def ask_chatgpt(user_input):
    gpt_question = {
        'role':'user',
        'content': user_input
    }
    history.append(gpt_question)
    
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages = history
    )

    gpt_response = {
        'role':'assistant',
        'content': response.choices[0].message.content
    }

    history.append(gpt_response)

    return gpt_response['content']


while True:
    user_input = input("[YOU]: ",)
    if user_input in {"exit", "quit", "종료", "그만", "끝"}:
        print("대화를 종료합니다.")
        break

    print("[챗봇 응답]: ", ask_chatgpt(user_input))