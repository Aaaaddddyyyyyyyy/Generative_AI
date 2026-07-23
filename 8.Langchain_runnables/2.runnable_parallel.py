from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel

load_dotenv()

prompt1= PromptTemplate(
    template='generate a tweet about a {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='generate a post on linkedin about {topic}',
    input_variables=['topic']
)

model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser= StrOutputParser()

parallel_chain=RunnableParallel({
    'tweet':RunnableSequence(prompt1,model,parser),
    'linkedin':RunnableSequence(prompt2,model,parser)
})

result=parallel_chain.invoke({'topic':'ai'})

print(result)