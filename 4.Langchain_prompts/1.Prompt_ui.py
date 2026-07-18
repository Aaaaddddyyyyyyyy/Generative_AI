from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

st.header("Research Tools")  ## header adds heading to web

user_input = st.text_input("Enter your Prompt here : ")  ## text_input takes input from user

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)