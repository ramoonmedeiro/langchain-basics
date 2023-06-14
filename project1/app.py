# env vars
from dotenv import load_dotenv, find_dotenv
import os

# streamlit lib
import streamlit as st

# utils
from utils import get_llm, get_answer


load_dotenv(find_dotenv())
open_ai_api_key = os.getenv("OPENAI_API_KEY")
llm = get_llm(open_ai_api_key=open_ai_api_key)


st.title("Simple QA App")

question = st.text_input(
    label="Ask everything",
)

submit = st.button(
    label='generate answer',
    key='generate answer')

if submit:
    answer = get_answer(llm=llm, question=question)
    st.subheader("Answer:")
    st.write(answer)
