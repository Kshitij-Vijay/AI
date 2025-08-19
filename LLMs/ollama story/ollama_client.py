from langchain_ollama import OllamaLLM

def get_model(model_name: str):
    """
    Return an Ollama model wrapped for LangChain.
    """
    return OllamaLLM(model=model_name)
