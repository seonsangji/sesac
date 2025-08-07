from langchain_core.prompts import PromptTemplate



template = "You are a naming consultant. Suggest a name for a web platform regarding with {project}"

prompt = PromptTemplate(
    input_variables=['product'],
    template=template
)

# filled_prompt = prompt.format(project="stock investment")
# print(filled_prompt)

# filled_prompt = prompt.format(project="real-time stock")
# print(filled_prompt)

# filled_prompt = prompt.format(project="icecream")
# print(filled_prompt)

test_projects = [
    "stock investment", "real-time stock", "icecream"
]


from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI()


for project in test_projects:
    p = prompt.format(project=project)
    result = llm.invoke(p).strip()
    print(result)