from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate # 이전에 배운 것
from langchain_core.prompts import ChatPromptTemplate # 이 모듈의 테마..
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.runnables import RunnableLambda

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# 1. 프롬프트 만들기 
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="You are a naming consultant for new companies"),
    HumanMessage(content="What is a good name for a {company} that makes {product}")
])

# 축약형
prompt_short = ChatPromptTemplate.from_messages({
    ('system', 'You are a naming consultant for new companies'),
    ('human', 'What is a good name for a {company} that makes {product}?')
})

# 2. 모델 생성하기
llm = ChatOpenAI(model='gpt-3.5-turbo-instruct') # chat 모델 중 하나 고르기
print(llm)

# 3. 파서 생성하기
parser = StrOutputParser()

# 4. (배운 것)입력값 정의하고 invoke 호출 하기 
chain = prompt | llm | parser | RunnableLambda(lambda x: {'response': x})

inputs = {'company': 'programming startup', 'product': 'real-time stock simulater'}
result = chain.invoke(inputs)

print("최종 결과:", result)