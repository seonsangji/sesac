import langchain
# langchain 과 openai 사 모델을 연동하려면 langhcain_openai
# langchain 과 claude 사 모델을 연동하려면 langhcain_claude

import os
from dotenv import load_dotenv

# from langchain.llms import OpenAI -> 구버전 API
from langchain_openai import OpenAI #-> 신버전

load_dotenv()

llm = OpenAI(max_token=1000) # 기본값 : gpt-3.5-turbo-instruct (2024.01)   # deprecated모델 : text-davinci-003 
print(llm)

prompt = "주식 시장의 파생 상품 종류는?"

result = llm.invoke(prompt)
print(result)