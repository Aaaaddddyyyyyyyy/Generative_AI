from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage    
load_dotenv()

model= ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chat_history= [SystemMessage(content='You are a helpful assistant.')]        ## stores the context for bot
while True:
    user_input= input("You: ")  ## text_input takes input from user
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=model.invoke(chat_history)  ## model.invoke takes the input and returns the output
    chat_history.append(AIMessage(content=result.text()))

    print("AdGPT",result.text())