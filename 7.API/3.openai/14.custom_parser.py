# LangChain Expression Language (LCEL) with RunnableLambda
from langchain_core.runnables import RunnableLambda
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

# 3. 나의 커스텀 아웃풋 파서 정의
def my_function(output):
    print("\nRAW 출력값은:")
    print(output)
    cleaned_output = output.strip().replace('"','').strip() 
    return {"final_response": cleaned_output}

# 4. 체인 만들기 ( prompt => llm => output )
# 여기서 정의한 lambda는 {"response": result} 의 형태로 담기 위한 커스텀함수이다.
chain = prompt | llm | RunnableLambda(my_function)

# 5. 결과 도출 ( 체인 실행 )
inputs = {'company': 'mock stock platform', 'project': 'simulating stock investment, additionally supporting making personal portfolio' } 

result = chain.invoke(inputs)

print(result)