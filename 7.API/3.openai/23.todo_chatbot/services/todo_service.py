# (약속)  _변수 : 내부변수다! 가져다 쓰지 마세요!

_todos = []
_next_id = 1

def get_all():
    return _todos

def get_all_to_string():
    return "\n".join([{"id": t["id"],"text":t["text"], "completed": t["done"]} for t in _todos])

def add(text):
    global _next_id
    new_todo = {
        'id': _next_id,
        'text': text,
        'completed': False
    }
    _todos.append(new_todo)
    _next_id += 1
    return new_todo

def toggle(todo_id):
    for todo in _todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            return todo
    return None

def delete(todo_id):
    for todo in _todos:
        if todo['id'] != todo_id:
            _todos.remove(todo)
            return todo
    return None