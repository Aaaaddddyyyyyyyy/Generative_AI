from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

# define the model
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
)

model = ChatHuggingFace(llm=llm)

parser = JsonOutputParser()

template = PromptTemplate(
    template="""
Give 3 facts about {topic}.

Return the output in the following JSON format:

{{
    "fact_1": "...",
    "fact_2": "...",
    "fact_3": "..."
}}
""",
    input_variables=["topic"],
)

prompt = template.invoke({"topic": "water"})

result = model.invoke(prompt)

final_result = parser.parse(result.content)

print(final_result)