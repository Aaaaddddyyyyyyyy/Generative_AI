from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import  PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda

load_dotenv()

def word_count(text):
    return len(text.split())
passthrough= RunnablePassthrough()

prompt1= PromptTemplate(
    template='generate a tweet about a {topic}',
    input_variables=['topic']
)
model=ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser= StrOutputParser()

joke_chain_gen=RunnableSequence(prompt1,model,parser)

parallel_chain=RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})


final_chain=RunnableSequence(joke_chain_gen,parallel_chain)

result=final_chain.invoke({'topic':'ai'}) 

print(result)