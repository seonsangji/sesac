# LangChain Expression Language (LCEL)

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

# 4. (생성기들을 연결한) 체인 만들기 = LCEL
chain = prompt | llm | parser

# 5. 결과 도출 ( 체인 실행 )
inputs = {'company': 'mock stock platform', 'project': 'simulating stock investment, additionally supporting making personal protpofilo' } 

result = chain.invoke(inputs)

print(F"최종결과:\n{result}")
