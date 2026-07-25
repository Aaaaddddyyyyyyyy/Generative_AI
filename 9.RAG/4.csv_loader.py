from langchain_community.document_loaders import CSVLoader

loader= CSVLoader(file_path='9.RAG\heart.csv')

docs=loader.load()

print(docs[1])
print(len(docs)) 