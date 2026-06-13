import requests
from core.config import OLLAMA_URL,MODEL_NAME

def ask_ollama(prompt:str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model":MODEL_NAME,
            "prompt":prompt,
            "stream":False
        }
    )

    result = response.json().get("response","No response")
    return result