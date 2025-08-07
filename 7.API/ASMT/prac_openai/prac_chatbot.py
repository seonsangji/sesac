import langchain

from dotenv import load_dotenv

from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI()

prompt = "어쩌구저쩌구"
result = llm.invoke(prompt)
print(result)