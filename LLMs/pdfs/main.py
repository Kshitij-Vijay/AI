from utils import get_pdf_path_via_dialog
from pdf_extractor import extract_pdf_content
from ollama_client import choose_model, create_vectorstore
from langchain_ollama import OllamaLLM
from langchain.chains import RetrievalQA

def main():
    print("Please select the PDF file to process.")
    pdf_path = get_pdf_path_via_dialog()

    print(f"[INFO] Extracting PDF content from: {pdf_path}")
    pdf_content = extract_pdf_content(pdf_path)

    print(f"[INFO] Extracted {len(pdf_content.texts)} text blocks, {len(pdf_content.images)} images, {len(pdf_content.tables)} tables.")

    # Combine all texts and tables into one large text for vectorstore creation
    combined_texts = "\n\n".join([tb.text for tb in pdf_content.texts] + [tbl.content for tbl in pdf_content.tables])

    # Select Ollama embedding model
    embed_model = choose_model("embedding")
    print(f"[INFO] Using embedding model: {embed_model}")

    # Create vectorstore from combined PDF text using Ollama embeddings
    vectorstore = create_vectorstore(combined_texts, model_name=embed_model)

    print("[INFO] Ready to answer questions. Enter 'exit' to quit.")

    
    # Step 2: Pick LLM
    llm_model = choose_model("llm")
    llm = OllamaLLM(model=llm_model)

    while True:
        query = input("Enter your question: ").strip()
        if query.lower() == "exit":
            break
        try:

            retriever = vectorstore.as_retriever()
            qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
            # Get top relevant contexts from vectorstore based on question
            relevant_docs = vectorstore.similarity_search(query, k=3)
            combined_context = "\n\n".join(doc.page_content for doc in relevant_docs)

            # Ask LLM using combined context and question
            answer = qa.invoke({"query": query})
            print("\nAnswer:", answer["result"])
        except Exception as e:
            print(f"[ERROR] {e}")

if __name__ == "__main__":
    main()
