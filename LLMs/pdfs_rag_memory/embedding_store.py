from typing import List, Tuple
import numpy as np

class EmbeddingStore:
    def __init__(self):
        self.store: List[Tuple[str, List[float], dict]] = []

    def add(self, content: str, embedding: List[float], metadata: dict):
        self.store.append((content, embedding, metadata))

    def similarity_search(self, query_emb: List[float], top_k=3):
        def cosine_sim(a, b):
            return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

        scored = [(content, cosine_sim(query_emb, emb), meta) for content, emb, meta in self.store]
        scored.sort(key=lambda x: x[1], reverse=True)
        return scored[:top_k]
