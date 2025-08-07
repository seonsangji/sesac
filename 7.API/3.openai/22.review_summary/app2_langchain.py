from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')
llm = ChatOpenAI()

summary_prompt = PromptTemplate.from_template("""
다음 목록을 기반으로 간결한 요약을 작성하시오.
                                              
리뷰목록: {reviews_text}                                              
""")

reviews=[] # 사용자 후기를 저장할 임시 데이터베이스.

translate_prompt = PromptTemplate.from_template(
    """다음 한국어 문장을 기반으로 {target_lang_name} 으로 번역하시오. 
    {summary_ko}
""")

summary_chain = summary_prompt | llm
translate_chain = translate_prompt | llm

from langchain_core.runnables import RunnableLambda, RunnablePassthrough

summary_then_translate_chain = {
    {
        "summary_ko": summary_prompt | llm | RunnableLambda(lambda m: m.content),
        "target_lang_name": RunnableLambda(lambda x: x['target_lang_name'])
        #: RunnablePassthrough()   와 같은 기능
    }
    | translate_prompt
    | llm
    | RunnableLambda(lambda m: m.content)
}

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
    # reviews 에 저장해놓은 리뷰 내용을 프런트에 불러오기.
    # DOM 에 렌더링하며 그리기
    return jsonify({'reviews':reviews})

@app.route('/api/ai-summary', methods=['GET'])
def get_ai_summary():
    target_lang = request.args.get('lang', 'ko')
    
    lang_name_map = {
        'ko': '한국어',
        'en': '영어',
        'ja': '일본어',
        'zh': '중국어',
        'fr': '프랑스어',
        'it': '이탈리아어'
    }

    lang_name = lang_name_map.get(target_lang, '영어')

    if not reviews:
        return jsonify({'summary': '리뷰가 없습니다.', 'averageRating': 0.0})
    average_rating = sum(review['rating'] for review in reviews) / len(reviews)
    reviews_text = '\n'.join([f"별점: {r['rating']}, 내용: {r['opinion']}" for r in reviews])

    # 체인 두개로 두 번 부르기

    response_summary = summary_chain.invoke({'reviews_text': reviews_text}).content

    response_translate = translate_chain.invoke({'summary_ko': response_summary, 'target_lang_name': lang_name}).content
    
    final_text = response_translate.choices[0].message.content.strip()

    # final_text = summary_then_translate_chain.invoke({'reviews_text': reviews_text, 'target_lang_name': lang_name})    # 체인 하나로 한 번 부르기


    return jsonify({
        'summary': final_text,
        'averageRating': average_rating
    })


if __name__ == '__main__':
    app.run(debug=True)