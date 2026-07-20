from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnableParallel
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableSequence

load_dotenv()

model1=ChatGoogleGenerativeAI(model='"gemini-3.5-flash"')
model2= ChatGroq(model="llama-3.3-70b-versatile")

prompt1= PromptTemplate(
    template='genrate short and simple notes from the following text \n {text}',
    input_variables=['text']
)


prompt2= PromptTemplate(
    template="generate 5 short question answer from text \n {text}",
    input_variables=['text']
)

prompt3= PromptTemplate(
    tempalte='merge the provided notes and quiz  into  a single document \n notes ->{notes} and quiz -> {quiz}',
    input_variables=['notes','quiz']
)

parser= StrOutputParser()

parallel_chain= RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})


merge_chain= prompt3 | model1 | parser

chain= parallel_chain | merge_chain         # merging both chains