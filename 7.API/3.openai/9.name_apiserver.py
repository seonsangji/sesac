from langchain_openai import OpenAI, ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

from dotenv import load_dotenv

from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__)

llm1 = OpenAI(temperature=0.9)
llm2 = ChatOpenAI(temperature=0.9)

@app.route('/api/name', methods=['POST'])
def generate_name():
    data = request.get_json()
    product = data.get('product')

    prompt = f"{product}을 판매하는 회사명을 지으려고 해. 회사명은 한글이고, 해당 {product}을 판매한다는 걸 알 수 있도록 직관적이지만, 너무 어색하지는 않았으면 좋겠어. 간결하고 적절한 걸로 회사명 1개만 제안해줘."

    result = llm1.invoke(prompt)
    names = result.strip()

    return jsonify({"product":product, "name": names})

@app.route('/api/name2', methods=['POST'])
def generate_name2():
    data = request.get_json()
    product = data.get('product')

    messages = [
        SystemMessage(content="당신은 브랜드명을 창의적으로 만드는 작명가입니다."),
        HumanMessage(content="{product}을 판매하는 회사명을 지으려고 해. 회사명은 영어고, 해당 {product}을 판매한다는 걸 알 수 있도록 직관적이면서도, 어색하지 않았으면 좋겠어. 간결하고 적절한 걸로 회사명 1개만 제안해줘.")
    ]

    result = llm2.invoke(messages)
    name = result.content.strip('"')

    return jsonify({"product":product, "name": name})


if __name__ == '__main__':
    app.run(debug=True)