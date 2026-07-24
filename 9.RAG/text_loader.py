from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

loader= TextLoader('9.RAG\demo.txt',encoding='utf-8')

docs=loader.load()       # load text file into document

#print(docs)
print(docs[0])