from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()

template = "You are a naming consultant. Suggest a name for a web platform regarding with {product}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

print("새 플랫폼명을 생성하는 서비스입니다. 종료하려면 'quit'을 입력하세요\n")

while True:
    product = input("제품/서비스를 입력하세요: ").strip()
    if product in {"quit"}:
        print("서비스를 종료합니다.")
        break

    filled_prompt = prompt.format(product=product)
    response = llm.invoke(filled_prompt)
    print("생성된 플랫폼명: ", response.strip(), "\n")

