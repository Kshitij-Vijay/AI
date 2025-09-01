import requests
from typing import List

NOMIC_API_KEY = "YOUR_NOMIC_API_KEY"
NOMIC_EMBEDDING_ENDPOINT = "https://api.nomic.ai/embedding"

def get_embedding(text: str) -> List[float]:
    headers = {
        "Authorization": f"Bearer {NOMIC_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {"text": text}
    response = requests.post(NOMIC_EMBEDDING_ENDPOINT, headers=headers, json=data)
    response.raise_for_status()
    embedding = response.json().get("embedding", [])
    return embedding
