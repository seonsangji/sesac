import openai
from dotenv import load_dotenv

from flask import Flask, render_template

app = Flask(__name__)

load_dotenv()
client = openai.OpenAI()

history = []

def ask_chatgpt(user_input):


while True:
    user_input = input("[YOU]: ",)
    if user_input in {"exit", "quit", "종료", "그만", "끝"}:
        print("대화를 종료합니다.")
        break
    print("[챗봇 응답]: ", ask_chatgpt(user_input))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask-chatgpt')
def ask_chatgpt(input):
    gpt_question = {
        'role': 'user',
        'content': input
    }
    history.append(gpt_question)
    response = client.chat.completions.create(
        model= 'gpt-4o',
        messages= history
    )
    gpt_response = {
        'role': 'assistant',
        'content': response.choices[0].message.content
    }
    history.append(gpt_response)

    return gpt_response['content']




if __name__ == '__main__':
    app.run(debug=True)

