from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.schema import Document

def create_vectorstore_from_text(lines, persist_directory="chromadb_dir"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    docs = [Document(page_content=line, metadata={"source": "medical_data"}) for line in lines]
    vectordb = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory=persist_directory
)
    return vectordb

def get_vector_results(vectordb, query, k=4):
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return retriever.get_relevant_documents(query)



