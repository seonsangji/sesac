from langchain_openai import OpenAI        # Completion 모델
from langchain_openai import ChatOpenAI    # Chat 모델 (QnA 모델 )

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(max_tokens=1000)              # gpt-3.5-turbo-instruct
prompt = "주식 시장의 파생 상품 종류는?"
result = llm.invoke(prompt)
print(result)


print('-' * 50)

llm2 = ChatOpenAI(model="gpt-3.5-turbo")   # gpt-3.5-turbo
result = llm2.invoke(prompt)
print(result.content)


print('-' * 50)

from langchain.schema import HumanMessage, SystemMessage, AIMessage
llm2 = ChatOpenAI(model="gpt-3.5-turbo")   
prompt = [
    SystemMessage(content="당신은 연애 상담가입니다."),
    HumanMessage(content="관심 있는 상대와 연락을 이어가려면?"),
    AIMessage(content="상대방과의 연락을 이어가기 위해서는 일정한 빈도로 연락을 주고받는 것이 중요합니다. 상대방을 너무 자주 연락하거나, 반대로 연락이 없는 것도 좋지 않습니다. 상대방의 반응을 주의 깊게 살펴보면서 적절한 빈도로 연락을 이어가는 것이 중요합니다."),
    HumanMessage(content="ㅜㅜ 연락을 12시간 만에 하는 거 어때.")
    ]   
result = llm2.invoke(prompt)
print(result.content)