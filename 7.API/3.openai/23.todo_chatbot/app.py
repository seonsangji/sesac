from flask import Flask, request, jsonify
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

from routes.chatbot_routes import chatbot_bp
from routes.todo_routes import todo_bp

app = Flask(__name__, static_folder='public', static_url_path='')

app.register_blueprint(chatbot_bp)
app.register_blueprint(todo_bp)


@app.route('/')
def index():
    return app.send_static_file('index.html')
# load_dotenv()

# llm = ChatOpenAI()

# prompt = ChatPromptTemplate.from_messages([
#     SystemMessage(content="나는 'todolist' 관리자로, 사용자의 일정을 안내하는 역할을 해."),
#     HumanMessage()
# ])

if __name__ == '__main__':
    app.run(debug=True)