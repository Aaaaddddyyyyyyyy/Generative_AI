from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
 
model=ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=1.6)
result=model.invoke("suggest me 5 indian female names")

print(result.text())