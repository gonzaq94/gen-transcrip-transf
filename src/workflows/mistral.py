import os
from mistralai import Mistral

# Set up API key for Mistral (assuming you get it after signing up)
API_KEY = os.getenv("MISTRAL_API_KEY")

# Mistral model version and parameters
MODEL_VERSION = "mistral-large-latest" #"mistral-7b"  # Adjust this to the model version you're using
TEMPERATURE = 0  # Lower temperature for more deterministic responses

# Function to call Mistral API
def call_mistral(query: str) -> str:

    client = Mistral(api_key=API_KEY)

    chat_response = client.chat.complete(
        model= MODEL_VERSION,
        messages = [
            {
                "role": "user",
                "content": query,
            },
        ]
    )

    return chat_response.choices[0].message.content