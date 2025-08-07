import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

history = [] 

def ask_chatgpt(user_input):

    gpt_systemprompt = {'role':'system', 'content': 'You are a computer programmer, developing platform'}
    gpt_question = {'role': 'user', 'content': user_input }

    if (len(history) == 0):
        history.append(gpt_systemprompt)
    history.append(gpt_question)

    print('실제로 우리가 지피티한테 물어보는 것\n----- 질문 시작 -----\n')
    print(history)
    print('-----여기까지-----')

    response = client.chat.completions.create(
        model= 'gpt-3.5-turbo',
        messages= history,
        temperature= 1.0
    )
    gpt_response = {'role': 'assistant', 'content': response.choices[0].message.content}
    history.append(gpt_response)

    return gpt_response


while True: 
    user_input = input("[YOU]: ", )
    if user_input in {"exit", "quit", "종료", "그만", "끝"}:
        print("대화를 종료합니다.")
        break

    print("[챗봇 응답]: ", ask_chatgpt(user_input))
