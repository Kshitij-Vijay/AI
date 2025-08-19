from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings


def create_vectorstore(text: str, model_name: str = "mistral"):
    """
    Create a searchable vectorstore from input text using embeddings.
    """
    # 1. Split text into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = splitter.split_text(text)

    # 2. Use Ollama embeddings
    embeddings = OllamaEmbeddings(model=model_name)

    # 3. Store chunks in FAISS
    vectorstore = FAISS.from_texts(chunks, embeddings)

    return vectorstore
