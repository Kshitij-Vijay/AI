from scraper import scrape_wikipedia
from dataset import build_dataset, load_dataset
from ollama_client import ask_ollama

# Step 1: Scrape and build dataset
url = input("Enter Wikipedia URL: ")
wiki_text = scrape_wikipedia(url)
chunks = build_dataset(wiki_text, chunk_size=100)  # 100-word chunks
print(f"Saved {len(chunks)} chunks to dataset!")

# Step 2: Query loop
while True:
    query = input("\nAsk a question (or type 'exit'): ")
    if query.lower() == "exit":
        break

    dataset = load_dataset()

    # Simple keyword search for relevant chunks
    relevant = [c["content"] for c in dataset if any(word.lower() in c["content"].lower() for word in query.split())]

    # If nothing found, just send everything
    context = "\n".join(relevant[:3]) if relevant else "\n".join(c["content"] for c in dataset[:3])

    answer = ask_ollama("llama2", context, query)
    print("\nAnswer:", answer)
