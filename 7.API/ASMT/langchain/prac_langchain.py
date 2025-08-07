from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


template = "You are a {field} expert. Give an explanation on {terminology}."

prompt = ChatPromptTemplate.from_messages([
    ('system',"You are English teacher, assessing the structure, flow, and fluency of users' sentences."),
    ('human', "this is my sentence: {dialogue}")
])

llm = ChatOpenAI(
    model='gpt-3.5-turbo',
    max_tokens=1000
    )

parser = StrOutputParser()

chain = prompt | llm | parser | RunnableLambda(lambda x:{'response': x})

inputs = {
    'dialogue': 'The man who I am interested in seems extrovert, but not that chatty in the messaging.'
}
result = chain.invoke(inputs)

print("최종 결과:", result)