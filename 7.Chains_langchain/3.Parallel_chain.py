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

chain= parallel_chain | merge_chain     # merging both chains


text="""The Samsung Galaxy S26 is an excellent compact flagship that focuses on refinement rather than reinvention. If you're coming from an S23 or older device, the upgrade feels worthwhile. If you're using an S25, however, the improvements are relatively modest. Reviewers consistently praise its display, performance, and software experience, while criticizing its battery life and charging speed

Pros
Premium compact design that is lightweight and comfortable for one-handed use.
Outstanding AMOLED display with a smooth 120Hz refresh rate, vibrant colors, and high brightness for outdoor visibility.
Fast flagship performance thanks to the latest chipset, making multitasking and gaming feel effortless.
Excellent One UI experience, with Galaxy AI features, useful customization, and long-term software support.
Reliable cameras, especially in daylight, with strong video quality and polished image processing.
Seven years of software updates, making it a good long-term investment.

Cons
25W charging is slow compared with many Android competitors offering 80W–120W charging.
Battery life is only average despite a larger battery, particularly under heavy use.
Camera hardware sees only incremental improvements, so users upgrading from the S25 may notice little difference.
Price increase makes the value proposition less compelling against rivals like the Pixel series or OnePlus.



"""    
result= chain.invoke({'text':text})