from flask import Flask, request, jsonify
from dotenv import load_dotenv

from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')

llm = OpenAI()

def gen_template(review_text, lang):
    return f"""다음 리뷰들의 상품에 대한 전반적인 평가를 한 문장으로 요약하시오.\n\n{review_text}\n\n 그 요약문을 {lang}으로 번역한 문장만 반환하시오."""
    
def gen_prompt(template):
    prompt = PromptTemplate(
        input_variables=['review', 'lang'], template=template)
    return prompt


def my_function(output):
    cleaned_ouput = output.strip()
    return {'final_response': cleaned_ouput}

reviews=[] # 사용자 후기를 저장할 임시 데이터베이스.

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/review', methods=['POST'])
def add_review():
    data = request.get_json()
    rating = data.get('rating')
    opinion = data.get('opinion')

    reviews.append({'rating': rating, 'opinion': opinion})
    print(rating, opinion)
    return jsonify({'message': '성공적으로 저장됨'})

@app.route('/api/review', methods=['GET'])
def get_review():
    #  reviews 에 저장해놓은 리뷰 내용을 프런트에 불러오기.
    #  DOM 에 렌더링하며 그리기
    return jsonify({'reviews':reviews})

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    
    # 미션 1. 프런트에서 보낸 언어 "코드값"으로, 원하는 언어로 매핑하기
    # 미션 2. 그걸 기반으로, gpt에게 번역 + 요약을 만들어 달라고 하기
    
    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})
    
    average_rating = sum(review['rating'] for review in reviews) / len(reviews)

    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])

    inputs = {
        'review': reviews_text,
        'lang': target_lang
    }

    chain = gen_prompt(gen_template(reviews_text, target_lang)) | llm | RunnableLambda(my_function)
    # try / catch 로 감쌀 것: key 없, 서버 죽, 돈 없음, 등등으로..
    review_result = chain.invoke(inputs)

    return jsonify({
        'summary': review_result['final_response'],
        'averageRating': average_rating
    })


if __name__ == '__main__':
    app.run(debug=True)