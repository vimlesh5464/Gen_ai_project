import streamlit as st
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# LLM
llm = ChatOpenAI(model_name="gpt-4o")  # latest syntax

# Prompt
prompt = PromptTemplate.from_template("""
Suggest top {number} high-demand skills for a {role} in {year}.
Experience level: {level}
""")

# Chain
chain = prompt | llm | StrOutputParser()

# Streamlit UI
st.title("AI Skill Advisor 🚀")

number = int(st.text_input("Number", "2"))
role = st.text_input("Role", "Backend Developer")
year = st.text_input("Year", "2025")
level = st.selectbox("Experience Level", ["Fresher", "Intermediate", "Expert"])

if st.button("Get Skills"):
    res = chain.invoke({
        "number": number,
        "role": role,
        "year": year,
        "level": level
    })
    st.success(res)
