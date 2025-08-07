from dotenv import load_dotenv
from openai import OpenAI
from services.todo_service import get_all_to_string, get_all, add, toggle, delete
from routes.todo_routes import get_todo, add_todo, toggle_todo, delete_todo
from flask import redirect, url_for, jsonify
import json


load_dotenv()

import os

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise RuntimeError("API키가 없습니다")


client = OpenAI()

def handle_chat(question):
    action = ask_gpt(question)
    final_response = do_action(action)

    return final_response


def ask_gpt(question):
    my_todo_list = get_all()
    system_prompt1 = f"""
    당신은 사용자의 TODO list 를 관리하는 비서입니다. 사용자의 질문에 대해 간결하게 답변해 주세요.\n\n

    [할일 목록]
    {my_todo_list}
"""
    
    system_prompt2 = f"""
    당신은 사용자의 TODO list 를 관리하는 비서입니다. 
    당신은 사용자의 질문에 대해 아래 중에 하나를 골라 action 을 선택하고 답변해야 합니다
    사용자의 TODO 항목과 질문에 대해 간결하게 답변해주세요.\n\n

    [출력 형식]
    {{"action": "add", "item": [항목]}} - 할 일을 추가해야 할 때
    {{"action": "list"}} - 할 일을 보여줘야 할 때
    {{"action": "update", "item": [항목ID]}} - 할 일을 수정해야 할 때 ( 다했거나, 이미 한 일이여도 다시 해야 할 때)
    {{"action": "delete", "item": [항목ID]}} - 할 일을 안 할 것이거나, 잘못 추가했을 때
    {{"action": "nothing"}} - assistant, 당신이 판단하기 어려울 때 또는 TODO 리스트의 항목이 없을 때

    [할일 목록]
    {my_todo_list}
"""
    
    system_prompt = system_prompt2
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role':'system', 'content': system_prompt},
            {'role':'user', 'content': question}
    ])

    reply = response.choices[0].message.content.strip()
    my_action = json.loads(reply)

    return my_action
    

def do_action(my_action):
    action = my_action.get('action')
    text = my_action.get('text')


    if action == 'add':
        add(text)
        return f'할 일 "{text}"를 추가하였습니다.'
    
    if action == 'delete':
        delete(text)
        return f'할 일 "{text}"를 삭제하였습니다.'
    
    if action == 'update':
        toggle(text)
        return f'할 일 "{text}"의 실행 여부를 수정하였습니다.'
    
    if action == 'list':
        my_todos = get_all_to_string()
        return f'다음 할 일들이 있습니다. \n{my_todos}'
    
    return f'잘 이해하지 못했습니다. TODO LIST에 관한 내용을 질문해 주세요.'











    my_action = json.loads(reply)
    if my_action.get('item'):
        item = my_action['item']
        if my_action['action'] == 'add':
            # redirect(url_for('/api/todo'))
            reply = {
                'item': item,
                'content': f"TODO 리스트에 {item}을 추가하였습니다." 
                }
        elif my_action['action'] == 'delete':
            delete_todo(item)
            reply = {
                'item': item,
                'content': f"TODO 리스트에 {item}을 추가하였습니다." 
                }
        elif my_action['action'] == 'update':
            toggle_todo(item)
            reply = {
                'item': item,
                'content': f"TODO 리스트에 {item}을 추가하였습니다." 
                }
    elif my_action['action'] == 'list':
        get_todo()
        reply = {'content': "TODO 리스트를 불러옵니다." }
    elif my_action['action'] == 'nothing':
        reply = {'content': "TODO 리스트에 관한 질문을 해주세요." }

    return reply

