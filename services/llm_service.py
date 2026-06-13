from  providers.ollama_provider import ask_ollama
from prompts.prompt import SYSTEM_PROMPT

def generate_response(user_query:str):
   full_prompt = SYSTEM_PROMPT + "\n\nUSER QUERY:\n" + user_query
   response = ask_ollama(full_prompt)

   return response

