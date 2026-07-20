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


model1=ChatGoogleGenerativeAI(model="gemini-3.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='classify the sentiment of following feedback text into positive or negative \n {feedback}',
    input_variables=['feedback']
)

classifier_chain= prompt1 | model1 | parser

print(classifier_chain.invoke({'feedback':'this is the terrible smartphone'}))
