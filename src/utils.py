import gradio as gr
from src.workflows.gemini import call_gemini
from workflows.gpt import call_gpt
from src.workflows.claude import call_claude
from src.workflows.mistral import call_mistral
import PyPDF2

MIN_NUMBER_WORDS = 6000

BASE_PROMPT = f"""
Your objective is to transform a given transcript into a teaching transcript that could be used by a course instructor to educate students on
the same topic. The input text contains a transcript of a speaker discussing a topic. The conversation may be casual and lack structure. Do not invent anything.
If the input text is meaningless or does not have any sense, just return a message asking the user to please input a meaningful text.
The output teaching transcript should be detailed, coherent, and logically structured. It should contain at least {MIN_NUMBER_WORDS} words (without spaces).
"""

# Define a function to process inputs and generate predictions
def generate_output(text: str, model_choice: str, temperature: float) -> str:
    query = f"{BASE_PROMPT}. Input text: \n\n {text} \n\n Output teaching transcript:"

    if model_choice == "Gemini":
        return call_gemini(query, temp=temperature)
    elif model_choice == "Claude":
        return call_claude(query, temp=temperature)
    elif model_choice == "GPT":
        return call_gpt(query, temp=temperature)
    elif model_choice == "Mistral":
        return call_mistral(query, temp=temperature)
    else:
        raise NotImplementedError(f"Model {model_choice} is not supported.")

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    with open(pdf_file.name, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text
