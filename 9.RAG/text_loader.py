from langchain_community.document_loaders import TextLoader

loader= TextLoader('D:\Langchain_models\requirements.txt',encoding='utf-8')

docs=loader.load()       # load text file into document

print(docs)
print(docs[0])