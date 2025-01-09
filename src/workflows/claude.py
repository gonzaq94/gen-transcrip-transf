import os
import anthropic
import tiktoken

# Set up API key for Claude
API_KEY = os.getenv("CLAUDE_API_KEY")
API_URL = "https://api.anthropic.com/v1/complete"

# Claude model version and parameters
MODEL_VERSION = "claude-3-5-sonnet-20241022"
MAX_TOKENS_CLAUDE = 8192

def get_num_tokens_claude(text: str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

# Function to call Claude API
def call_claude(base_prompt: str, input_text: str, temp: float = 0) -> str:

    query = f"{base_prompt}. Input text: \n\n {input_text} \n\n Output teaching transcript:"

    client = anthropic.Anthropic(
        api_key=API_KEY,
    )
    message = client.messages.create(
        model=MODEL_VERSION,
        temperature=temp,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return message