from dotenv import load_dotenv

from openai import OpenAI
from flask import Flask, request, jsonify

load_dotenv()

app = Flask(__name__, static_folder='public', static_url_path='')
openai = OpenAI()

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


    # try / catch 로 감쌀 것: key 없, 서버 죽, 돈 없음, 등등으로..
    response = openai.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{
            'role': 'user',
            'content': f'\n 리뷰들: {reviews_text} \n 선택 언어: {target_lang} \n 위 리뷰들을 선택한 언어로 번역해서 전반적인 의견이 어떤지 정리해줘. 이때 번역한 언어로 딱 한 문장으로 답장 부탁해'
        }]
    )

    print(response)

    summary = response.choices[0].message.content.strip()

    return jsonify({
        'summary': summary,
        'averageRating': average_rating
    })


if __name__ == '__main__':
    app.run(debug=True)