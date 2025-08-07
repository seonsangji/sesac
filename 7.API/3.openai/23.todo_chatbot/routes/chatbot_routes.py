from flask import Blueprint, request, jsonify
from services.chatbot_service import handle_chat
from services.todo_service import get_all
import json

chatbot_bp = Blueprint('chatbot', __name__)


@chatbot_bp.route('/api/chat', methods=['POST'])
def chatbot_response():
    data = request.get_json()
    question = data.get('user_input')
    result = handle_chat(question)

    # result = ask_gpt(question).get('content', None)
    # item = ask_gpt(question).get('item', None)
    return jsonify({'chatbot': f'{result}'})

