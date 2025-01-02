import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_VERSION = "gemini-1.5-flash"
TEMPERATURE = 0  # the smaller the temperature, the lower the variability in the response


def call_gemini(query: str) -> str:
    model = genai.GenerativeModel(MODEL_VERSION)
    response = model.generate_content(
        query,
        generation_config=genai.types.GenerationConfig(temperature=TEMPERATURE),
        stream=False
    )

    return response.text

def main():

    with open("example.txt", "r") as file:
        text = file.read()

    out = call_gemini(text)

    print(out)

    print(f"Out number of words: {len(text.split())}")

if __name__ == "__main__":
    main()