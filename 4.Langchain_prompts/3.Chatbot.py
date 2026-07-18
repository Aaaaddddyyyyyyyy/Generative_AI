from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash")

while True:
    user_input= input("You: ")  ## text_input takes input from user
    if user_input=='exit':
        break
    result=model.invoke(user_input)

    print("AdGPT",result.text())