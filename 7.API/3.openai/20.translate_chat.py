from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

template = "다음 문장을 한국어로 번역하시오.\n\n{article}"
prompt = ChatPromptTemplate.from_messages([         SystemMessagePromptTemplate.from_template("당신은 번역 전문가입니다."),
HumanMessagePromptTemplate.from_template(template)]
)

llm = ChatOpenAI(temperature=0.5)

chain = prompt | llm | RunnableLambda(lambda x:{"translated": x.content.strip()})

input_text = {
    'article': '''
Throwing pedals like do you love me or not
Head is spinning and it don't know when to stop
Cause you said forever babe did you mean it or not
Hold on hold on
You leave me on read babe but I still get the message
Instead of a line its 3 dots but I can connect em
And if it ain't right babe
You know I respect it
    '''
}

result = chain.invoke(input_text)
print("최종결과: ", result)
# lines = result['summary'].split('\n')
# for line in lines:
