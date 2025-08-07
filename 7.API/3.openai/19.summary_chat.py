from dotenv import load_dotenv

from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableLambda

load_dotenv()

template = "다음 문장을 3줄로 요약하시오.\n\n{article}"
prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 장문을 적절하게 요약할 수 있습니다."),
    HumanMessagePromptTemplate.from_template(template)
    ])

llm = ChatOpenAI(temperature=0.5)


print_line_by_line = RunnableLambda(
    lambda x: {
        'summary': [line.strip() for line in x.split('\n') if line.strip()]
    }
)

chain = prompt | llm | #

input_text = {
    'article': '''
    최근 국가공무원인재개발원(연수원)에서 교육받고 있는 예비 사무관들이 각자 지망하는 부처를 조사해 보니, 해양수산부가 중앙부처 17개 중 일반행정 직렬 기준 경쟁률 ‘꼴찌’를 기록했다고 합니다. 예비 사무관들은 1지망부터 3지망까지 부처 3개를 순서대로 적어서 냈는데, 3지망 내에 해수부를 포함시킨 예비 사무관은 11명이었습니다. 해수부가 계획한 선발 인원(6명)의 1.83배에 그치는 수준입니다. 경쟁률이 2배를 못 넘은 부처는 중앙부처 가운데 해수부가 유일합니다.

불과 3년 전인 2022년까지만 해도 일반행정 직렬에서 수석을 차지한 예비 사무관이 1지망으로 선택한 부처가 해수부였을 정도로 해수부는 인기 부처 중 하나였습니다. 바다와 관련된 업무를 맡다 보니 국제 무대에서 활약할 기회가 많고 정치적으로 민감한 업무가 주어지는 경우는 드물어, ‘MZ세대’ 젊은 직원의 선호도가 높았다는 것입니다. 기획재정부나 산업부처럼 규모가 큰 부처보다 업무 부담이 적고 승진은 빠르다는 점도 인기 요인이었습니다.

관가에서는 올해 해수부가 부산으로 이전하게 되면서 ‘찬밥 신세’가 됐다는 이야기가 나옵니다. 앞으로 해수부 직원들은 국회에 정부 사업을 설명하거나 기재부와 예산 협의를 하기 위해 부산에서 서울·세종을 수시로 오가야 합니다. 양식장이 밀집한 전남, 물류 거점 중 하나인 평택항·인천항 등으로의 출장 경로도 더욱 복잡해졌습니다. 부산에 연고가 있지 않은 한 결혼과 육아, 주거 문제도 눈앞의 고민거리입니다. 예비 사무관들로선 굳이 해수부를 따라 부산까지 가서 수고로움을 감내할 이유가 없다는 것입니다.


정부도 해수부가 기피 부처로 전락할 것이란 점을 예상하지 못한 건 아닙니다. 전재수 해수부 장관은 후보자 시절 “해수부가 부산으로 가면 우수 인재가 해수부를 기피할 것이란 우려가 상당한 것을 안다”며 “특별한 희생에 특별한 보상을 할 것”이라고 했습니다. 그러나 해수부 내에선 “5년 후에나 열릴 북극항로 때문에 올해 부산으로 급히 내려가야 한다는 논리부터 설득이 안 되는데 ‘보상’이 무슨 소용이냐”는 불만이 나옵니다. 해수부가 부산으로 내려가서 하게 되는 일이 무엇인지, 어떠한 보람을 느낄 수 있는지부터 설명이 돼야 인재들의 마음을 돌릴 수 있을 것입니다.
    '''
}

result = chain.invoke(input_text)
print("최종결과: ", result)
# lines = result['summary'].split('\n')
# for line in lines:
