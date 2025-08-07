from flask import Flask, request, send_from_directory, jsonify

import openai
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI()

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    print(data)
    userInput = data['userInput']
    chatbot_response = ask_chatgpt(userInput)
    return jsonify({"response": f" {chatbot_response}"})

history = [] # 전역 변수에 대화 내용 모두 저장 : 사용자별 분리 불가능.

def ask_chatgpt(user_input):

    history.append({'role':'user', 'content': user_input})

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages= history,
        temperature = 1.0
    )

    chatgpt_response = response.choices[0].message.content

    history.append({'role':'assistant', 'content': chatgpt_response})

    if len(history) > 10:
        history.pop(0)
        history.pop(0)

    print(history)
    print('대화 내용 길이: ', len(history))

    return chatgpt_response

if __name__ == '__main__':
    app.run(debug=True)

