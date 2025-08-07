from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_openai import OpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

template = "아래 수신자에게 보낼 메일을 회사 메뉴얼에 맞게 작성해주세요. 메일 내용은 아래 주제를 다루고 있습니다.\n\n수신자: {recipient}\n\n주제: {topic}"
prompt = PromptTemplate(input_variables=["recipient", "topic"], template=template)

llm = OpenAI(temperature=1.0, max_tokens=1000)

chain = prompt | llm | RunnableLambda(lambda x:{"email": x.strip()})

input_text = {
    'recipient': '인사팀',
    'topic': '탕비실 간식 부족의 원흉이 인사팀 내부에 있음'
}

result = chain.invoke(input_text)
print("최종결과: ", result)
# lines = result['summary'].split('\n')
# for line in lines:
