import openai
from dotenv import load_dotenv

from flask import Flask, render_template, request

app = Flask(__name__)

load_dotenv()

client = openai.OpenAI()

history = []

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask-chatgpt', methods=["POST"])
def ask_chatgpt():
    data = request.get_json()
    question = data.get('question')
    gpt_question = {
        'role': 'user',
        'content': question
    }
    history.append(gpt_question)
    response = client.chat.completions.create(
        model= 'gpt-4o',
        messages= history
    )
    print(response)
    gpt_response = {
        'role': 'assistant',
        'content': response.choices[0].message.content
    }
    history.append(gpt_response)

    return gpt_response['content']





if __name__ == '__main__':
    app.run(debug=True)

