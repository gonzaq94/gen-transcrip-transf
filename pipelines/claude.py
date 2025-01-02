import os
import requests
import anthropic

# Set up API key for Claude
API_KEY = os.getenv("CLAUDE_API_KEY")
API_URL = "https://api.anthropic.com/v1/complete"

# Claude model version and parameters
MODEL_VERSION = "claude-3-5-sonnet-20241022"  # Replace with the specific model you are using
TEMPERATURE = 0  # the smaller the temperature, the lower the variability in the response

# Function to call Claude API
def call_claude(query: str) -> str:

    client = anthropic.Anthropic(
        api_key=API_KEY,
    )
    message = client.messages.create(
        model=MODEL_VERSION,
        max_tokens=1024,
        messages=[
            {"role": "user", "content": query}
        ]
    )

    return message

# Main function
def main():
    # Read the input text
    with open("example.txt", "r") as file:
        text = file.read()

    # Call Claude with the text input
    out = call_claude(text)

    # Print the output
    print(out)

    # Print the number of words in the input text
    print(f"Input number of words: {len(text.split())}")
    print(f"Output number of words: {len(out.split())}")

if __name__ == "__main__":
    main()
