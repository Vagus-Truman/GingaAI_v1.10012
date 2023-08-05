import openai
from asgiref.sync import sync_to_async
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("ChatGPT_API_Key")
openai.api_base = "http://127.0.0.1:8000/v1"

async def chatgpt_response(prompt):
    response = await sync_to_async(openai.Completion.create)(
        
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.5,
        max_tokens = 64
        
    )
    
    response_dictionary = response.get("choices")
    if response_dictionary and len(response_dictionary) > 0:
        prompt_response = response_dictionary[0]["text"]
    return prompt_response