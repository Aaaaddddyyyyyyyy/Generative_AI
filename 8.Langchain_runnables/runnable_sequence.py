from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnablesSequence

load_dotenv()

prompt= PromptTemplate(

    teplate='write a joke about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser= StrOutputParser()

chain= RunnablesSequence(prompt,model,parser)

result=chain.invoke({"topic":"ai"})

print(result)