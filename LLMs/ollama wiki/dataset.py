import json
import os

DATASET_FILE = "data/wiki_dataset.json"

def save_dataset(chunks):
    os.makedirs("data", exist_ok=True)
    with open(DATASET_FILE, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

def load_dataset():
    if not os.path.exists(DATASET_FILE):
        return []
    with open(DATASET_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def build_dataset(text: str, chunk_size: int = 500):
    """Split text into chunks for later retrieval."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk_text = " ".join(words[i:i+chunk_size])
        chunks.append({
            "id": len(chunks) + 1,
            "content": chunk_text
        })
    save_dataset(chunks)
    return chunks
