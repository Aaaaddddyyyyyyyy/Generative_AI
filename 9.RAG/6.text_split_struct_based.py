from langchain_text_splitters import RecursiveCharacterTextSplitter

text="""
In Retrieval-Augmented Generation (RAG), text structure–based splitting is a strategy for chunking documents into meaningful segments before embedding and storing them in a vector database. Instead of splitting purely by token count or fixed length, this method leverages the inherent structure of the text (like headings, paragraphs, or semantic boundaries) to preserve context.

"""

# initialize the splitter
splitter= RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,

)

# perform the splitting
chunks= splitter.split_text(text)

print(len(chunks))
print(chunks)