from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.5-flash')

prompt= PromptTemplate(
    template='Answer the following question \n{question} from following text -\n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url='https://www.flipkart.com/apple-macbook-air-m5-2026-m5-16-gb-512-gb-ssd-tahoe-mdh74hn-a/product-reviews/itm7780abdd2be7d?pid=COMHH78Y2WQUBPWE&lid=LSTCOMHH78Y2WQUBPWEGUFZGA&sortOrder=MOST_HELPFUL&certifiedBuyer=false&aid=overall&pageUID=1784945881369'

loader=WebBaseLoader(url)   

docs= loader.load()

print(docs)
print(len(docs))