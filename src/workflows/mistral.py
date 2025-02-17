import os
from mistralai import Mistral
import tiktoken

# Set up API key for Mistral (assuming you get it after signing up)
API_KEY = os.getenv("MISTRAL_API_KEY")

# Mistral model version and parameters
MODEL_VERSION = "mistral-large-latest" #"mistral-7b"  # Adjust this to the model version you're using
MAX_TOKENS_MISTRAL = 8192


def get_num_tokens_mistral(text: str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

# Function to call Mistral API
def call_mistral(base_prompt: str, input_text: str, temp: float = 0) -> str:

    query = f"{base_prompt}. Input text: \n\n {input_text} \n\n Output teaching transcript:"

    client = Mistral(api_key=API_KEY)

    chat_response = client.chat.complete(
        model= MODEL_VERSION,
        messages = [
            {
                "role": "user",
                "content": query,
            },
        ],
        temperature=temp
    )

    return chat_response.choices[0].message.content