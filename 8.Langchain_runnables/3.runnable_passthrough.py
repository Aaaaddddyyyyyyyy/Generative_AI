from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough

load_dotenv()

passthrough= RunnablePassthrough()

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

joke_gen_chain= RunnableSequence(prompt1,model,parser)

parallel_chain= RunnableParallel({
    'joke': RunnablePassthrough(),
    'explaination': RunnableSequence(prompt2,model,parser)
})

final_chain=RunnableSequence(joke_gen_chain,parallel_chain)

result=final_chain.invoke({'topic':'cricket'})

print(result)