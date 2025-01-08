import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_VERSION = "gemini-1.5-flash"
TEMPERATURE = 0  # the smaller the temperature, the lower the variability in the response


def call_gemini(query: str) -> str:
    model = genai.GenerativeModel(MODEL_VERSION)

    # get number of tokens

    number_tokens = model.count_tokens(query)

    print(number_tokens)

    response = model.generate_content(
        query,
        generation_config=genai.types.GenerationConfig(temperature=TEMPERATURE),
        stream=False
    )

    return response.text
