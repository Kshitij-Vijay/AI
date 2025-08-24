from dataset import create_vectorstore
from langchain.chains import RetrievalQA
from langchain_ollama import OllamaLLM
import os
import ollama

ollama_host = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
client = ollama.Client(host=ollama_host)


def choose_model(model_type="llm"):
    resp = ollama.list()
    print("Ollama list response:", resp)
    models = resp.get("models", [])
    ...

    models = ollama.list()["models"]

    # Filter models by type
    if model_type == "embedding":
        models = [m.model for m in models if "embed" in m.model.lower()]
    else:
        models = [m.model for m in models if "embed" not in m.model.lower()]


    if not models:
        print(f"No {model_type} models found in Ollama. Please pull some first!")
        exit(1)

    print(f"\nAvailable {model_type.upper()} models:")
    for idx, model in enumerate(models, 1):
        print(f"{idx}. {model}")

    choice = int(input(f"Select a {model_type} model [1-{len(models)}]: "))
    return models[choice - 1]

def main():
    story = input("Enter your story:\n")

    # Step 1: Pick embedding model
    embed_model = choose_model("embedding")
    vectorstore = create_vectorstore(story, model_name=embed_model)

    # Step 2: Pick LLM
    llm_model = choose_model("llm")
    llm = OllamaLLM(model=llm_model)

    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break
        answer = qa.invoke({"query": query})
        print("\nAnswer:", answer["result"])

if __name__ == "__main__":
    main()
