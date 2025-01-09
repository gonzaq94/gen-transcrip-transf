import os
from mistralai import Mistral

# Set up API key for Mistral (assuming you get it after signing up)
API_KEY = os.getenv("MISTRAL_API_KEY")

# Mistral model version and parameters
MODEL_VERSION = "mistral-large-latest" #"mistral-7b"  # Adjust this to the model version you're using
MAX_TOKENS_MISTRAL = 1048576


def get_num_tokens_mistral(text: str) -> int:
    pass

# Function to call Mistral API
def call_mistral(query: str, empty_query: str, temp: float = 0) -> str:

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