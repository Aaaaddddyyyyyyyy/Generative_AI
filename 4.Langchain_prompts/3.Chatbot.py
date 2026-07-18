from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chat_history= []        ## stores the context for bot
while True:
    user_input= input("You: ")  ## text_input takes input from user
    chat_history.append(user_input)
    if user_input=='exit':
        break
    result=model.invoke(user_input)
    chat_history.append(result.text())

    print("AdGPT",result.text())