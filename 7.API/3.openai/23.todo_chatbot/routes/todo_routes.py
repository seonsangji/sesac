from flask import Blueprint, request, jsonify
from services import todo_service as svc


todo_bp = Blueprint('todo', __name__)


@todo_bp.route('/api/todo', methods=['GET'])
def get_todo():
    return jsonify(svc.get_all())


@todo_bp.route('/api/todo', methods=['POST'])
def add_todo():
    data = request.get_json()
    text = data.get('text')
    svc.add(text)
    return jsonify({'success': '성공적으로 추가됨'})


@todo_bp.route('/api/todo/<int:todo_id>', methods=['PUT'])
def toggle_todo(todo_id):
    result = svc.toggle(todo_id)
    if result:
        return jsonify({'success': 'toggle 완료'})
    return jsonify({'error':'Todo not found'})


@todo_bp.route('/api/todo/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    result = svc.delete(todo_id)
    if result:
        return jsonify({'result':'Todo successfully deleted'})
    return jsonify({'error':'Todo not found'})