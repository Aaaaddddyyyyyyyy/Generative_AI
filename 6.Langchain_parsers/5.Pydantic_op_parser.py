from langchain_huggingface  import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

load_dotenv()

# define the model

llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)   

class Person(BaseModel):

    name:str = Field(description='name of the person')
    age : int= Field(gt=18,description='age of the person')
    city : str= Field(description='name of the city person belongs to')

parser= PydanticOutputParser(pydantic_object=Person)

template= PromptTemplate(
    template='Generate the name,age,city of the fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain= template | model | parser

final_result= chain.invoke({'place':'australian'})

print(final_result)