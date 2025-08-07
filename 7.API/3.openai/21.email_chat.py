from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

template = "아래 수신자에게 보낼 메일을 회사 메뉴얼에 맞게 작성해주세요. 메일 내용은 아래 주제를 다루고 있습니다.\n\n수신자: {recipient}\n\n주제: {topic}"
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(
        "당신은 사내 소통에 능하며 사회초년생에게 조언을 주는 대인관계 전문가입니다." 
        "이를 바탕으로 업무 이메일을 명확하고 정중하게 쓸 수 있습니다."),
    HumanMessagePromptTemplate.from_template(template)
])

llm = ChatOpenAI(temperature=1.0, max_tokens=1000)

chain = prompt | llm | RunnableLambda(lambda x:{"email": x.content.strip()})

input_text = {
    'recipient': '인사팀',
    'topic': '육아 휴직 사원의 업무를 다른 사원에게 배분시켜, 사내 불만이 제기되고 휴직 사원은 눈치를 보게 되었다. 육아 휴직 발생의 경우 사내 업무 분할을 효율적으로 해줄 것을 요청함.'
}

result = chain.invoke(input_text)
print("최종결과: ", result['email'])
# lines = result['summary'].split('\n')
# for line in lines:
