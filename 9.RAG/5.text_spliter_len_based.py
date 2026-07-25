from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader= PyPDFLoader('9.RAG\ai.pdf')

docs=loader.load()


text="""A common mistake is treating the symptom (noise) with spray instead of fixing the worn part. If the noise has started recently, it's more likely that cleaning or replacing a worn component is the real solution.

"""
splitter=CharacterTextSplitter(
        chunk_size=10,
        chunk_overlap=0,
        separator=''
)

#result=splitter.split_text(text)

result=splitter.split_documents(docs)
print(result)
