import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_VERSION = "gemini-1.5-flash"
MAX_TOKENS_GEMINI = 1048576

def get_num_tokens_gemini(text: str) -> int:
        
    model = genai.GenerativeModel(MODEL_VERSION)

    return model.count_tokens(text)

def call_gemini(base_prompt: str, input_text: str, temp: float = 0) -> str:

    query = f"{base_prompt}. Input text: \n\n {input_text} \n\n Output teaching transcript:"

    model = genai.GenerativeModel(MODEL_VERSION)

    response = model.generate_content(
        query,
        generation_config=genai.types.GenerationConfig(temperature=temp),
        stream=False
    )

    return response.text
