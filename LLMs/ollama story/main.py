from dataset import create_vectorstore
from ollama_client import get_model
from langchain.chains import RetrievalQA

import ollama

def list_models():
    response = ollama.list()
    # show available models
    print("\nAvailable Models:")
    for i, m in enumerate(response["models"], start=1):
        print(f"{i}. {m['model']}")
    return [m["model"] for m in response["models"]]

def main():
    # Step 1: List models and select one
    models = list_models()
    choice = int(input("\nSelect a model number: ")) - 1
    model_name = models[choice]
    print(f"\n✅ Using model: {model_name}")

    # Step 2: Input story
    story = input("\nEnter your story (paste big text if needed):\n")

    # Step 3: Build dataset
    vectorstore = create_vectorstore(story, model_name=model_name)

    # Step 4: Setup retriever + QA chain
    llm = get_model(model_name)
    retriever = vectorstore.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

    # Step 5: Ask questions
    print("\nYou can now ask questions about your story! (type 'exit' to quit)")
    while True:
        query = input("\nQuestion: ")
        if query.lower() == "exit":
            break
        answer = qa.run(query)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
