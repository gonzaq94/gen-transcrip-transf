import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

MODEL_VERSION = "gemini-1.5-flash"
MAX_TOKENS_GEMINI = 8192

def get_num_tokens_gemini(text: str) -> int:
        
    model = genai.GenerativeModel(MODEL_VERSION)

    return model.count_tokens(text).total_tokens

def call_gemini(base_prompt: str, input_text: str, temp: float = 0) -> str:

    query = f"{base_prompt}. Input text: \n\n {input_text} \n\n Output teaching transcript:"

    model = genai.GenerativeModel(MODEL_VERSION)

    response = model.generate_content(
        query,
        generation_config=genai.types.GenerationConfig(temperature=temp),
        stream=False
    )

    return response.text

def validate_text(input_text: str):

    query = f"""
    You will get as input some text. You need to decide if the next is meaningless. Input text: \n\n {input_text} \n\n Output a binary answer, either 'yes' if the input text is valid, or 'no' if it is meaningless:
    """

    model = genai.GenerativeModel(MODEL_VERSION)

    response = model.generate_content(
        query,
        generation_config=genai.types.GenerationConfig(temperature=0),
        stream=False
    )

    return response.text