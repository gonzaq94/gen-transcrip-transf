import os
from typing import Optional
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL_VERSION = "gpt-4o-mini"
TEMPERATURE = 0
def call_gpt(query: str, temp: float = 0) -> Optional[str]:

    client = openai.OpenAI()

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": query,
            }
        ],
        model=MODEL_VERSION,
        temperature=temp
    )

    return response.choices[0].message.content