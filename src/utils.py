import gradio as gr
from src.workflows.gemini import call_gemini, get_num_tokens_gemini, MAX_TOKENS_GEMINI
from workflows.gpt import call_gpt, get_num_tokens_gpt, MAX_TOKENS_GPT
from src.workflows.claude import call_claude, get_num_tokens_claude, MAX_TOKENS_CLAUDE
from src.workflows.mistral import call_mistral, get_num_tokens_mistral, MAX_TOKENS_MISTRAL
import PyPDF2

MIN_NUMBER_WORDS = 6000

BASE_PROMPT = f"""
Your objective is to transform a given transcript into a teaching transcript that could be used by a course instructor to educate students on
the same topic. The input text contains a transcript of a speaker discussing a topic. The conversation may be casual and lack structure. Do not invent anything.
If the input text is meaningless or does not have any sense, just return a message asking the user to please input a meaningful text.
The output teaching transcript should be detailed, coherent, and logically structured. It should contain at least {MIN_NUMBER_WORDS} words (without spaces).
"""

def split_text_in_chunks(text: str, tokens_empty_prompt: int, tokens_text: int, max_n_tokens: int) -> list[str]:

    return [text]

# Define a function to process inputs and generate predictions
def generate_output(text: str, model_choice: str, temperature: float) -> str:

    if model_choice == "Gemini":
        call_llm = call_gemini
        get_num_tokens = get_num_tokens_gemini
        max_n_tokens = MAX_TOKENS_GEMINI
    elif model_choice == "Claude":
        call_llm = call_claude
        get_num_tokens = get_num_tokens_claude
        max_n_tokens = MAX_TOKENS_CLAUDE
    elif model_choice == "GPT":
        call_llm = call_gpt
        get_num_tokens = get_num_tokens_gpt
        get_num_tokens = MAX_TOKENS_GPT
    elif model_choice == "Mistral":
        call_llm = call_mistral
        get_num_tokens = get_num_tokens_mistral
        get_num_tokens = MAX_TOKENS_MISTRAL
    else:
        raise NotImplementedError(f"Model {model_choice} is not supported.")
    
    tokens_empty_prompt = get_num_tokens(f"{BASE_PROMPT}. Input text: \n\n \n\n Output teaching transcript:")
    tokens_text = get_num_tokens(text)

    if tokens_empty_prompt + tokens_text < max_n_tokens:
        return call_llm(BASE_PROMPT, text, temp=temperature)
    else:
        text_chunks = split_text_in_chunks(text, tokens_empty_prompt, tokens_text, max_n_tokens)
        out = """"""
        for chunk in text_chunks:
            out += call_llm(BASE_PROMPT, chunk, temp=temperature)
        return out

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file.name, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text
