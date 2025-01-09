import os
from typing import Optional
import openai
import tiktoken

openai.api_key = os.getenv("OPENAI_API_KEY")

MODEL_VERSION = "gpt-4o-mini"
MAX_TOKENS_GPT = 8192  # For GPT-4 8k

def get_num_tokens_gpt(text: str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def call_gpt(base_prompt: str, input_text: str, temp: float = 0) -> Optional[str]:

    query = f"{base_prompt}. Input text: \n\n {input_text} \n\n Output teaching transcript:"

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