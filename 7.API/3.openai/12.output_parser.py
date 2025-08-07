from langchain_core.output_parsers import StrOutputParser, CommaSeparatedListOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. 프롬프트 생성기 만들기
template = """You are a naming consultant. 
Suggest 5 good names for a {company} regarding with {project}
"""

prompt = PromptTemplate(
    input_variables=['company', 'project'],
    template=template
)

# 2. 모델 생성기 만들기 ( 추가로 모델, 키, 온도 등 설정 가능하다 )
llm = OpenAI() 

# 3. 출력 파서를 생성한다
parser = StrOutputParser()
parser_csv = CommaSeparatedListOutputParser()

# 4. 결과 도출 ( 위의 생성기들을 연결한다 : prompt -> llm에 넣기 -> output 파서 )
inputs = {'company': 'mock stock platform', 'project': 'simulating stock investment' } 

filled_prompt = prompt.format(**inputs)
llm_output = llm.invoke(filled_prompt)


result_str = parser.invoke(llm_output)
result_csv = parser.invoke(llm_output)

print('문자열로 파싱: \n', result_str)
print('CSV 리스트로 파싱: \n', result_csv)