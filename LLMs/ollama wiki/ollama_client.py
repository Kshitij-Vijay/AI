import ollama

def ask_ollama(model: str, context: str, query: str) -> str:
    prompt = f"""
You are a helpful assistant. Use the following context to answer the question.

Context:
{context}

Question:
{query}
"""
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]
