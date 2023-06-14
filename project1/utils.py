from langchain.llms import OpenAI


def get_llm(open_ai_api_key: str) -> OpenAI:

    llm = OpenAI(
        model='text-davinci-003',
        temperature=0,
        openai_api_key=open_ai_api_key
    )

    return llm


def get_answer(llm: OpenAI, question: str) -> str:

    answer = llm(question)

    return answer
