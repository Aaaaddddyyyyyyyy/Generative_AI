from langchain_community.document_loaders  import PyPDFLoader

loader = PyPDFLoader("9.RAG/ai.pdf")
docs=loader.load()

print(docs)

print(docs[1].metadata)
print(docs[0].page_content)