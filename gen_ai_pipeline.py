import gradio as gr
from pipelines.gemini import call_gemini
from pipelines.gpt2 import call_gpt2
from pipelines.claude import call_claude
from pipelines.mistral import call_mistral
import PyPDF2

MIN_NUMBER_WORDS = 6000

BASE_PROMPT = f"""
Your objective is to transform a given transcript into a teaching transcript that could be used by a course instructor to educate students on
the same topic. The input text contains a transcript of a speaker discussing a topic (e.g., cybersecurity,
machine learning, or marketing). The conversation may be casual and lack structure.
The output teaching transcript should be detailed, coherent, and logically structured. It should contain at least {MIN_NUMBER_WORDS} words (without spaces).
"""

# Define a function to process inputs and generate predictions
def generate_output(text: str, model_choice: str) -> str:
    query = f"{BASE_PROMPT}. Input text: \n\n {text} \n\n Output teaching transcript:"

    if model_choice == "Gemini":
        return call_gemini(query)
    elif model_choice == "Claude":
        return call_claude(query)
    elif model_choice == "GPT-2":
        return call_gpt2(query)
    elif model_choice == "Mistral":
        return call_mistral(query)
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

# Function to handle both input types (text or PDF)
def process_input(input_type, input_data_text, input_data_pdf, model_choice):
    if input_type == "Text":
        return generate_output(input_data_text, model_choice)
    elif input_type == "PDF":
        extracted_text = extract_text_from_pdf(input_data_pdf)
        return generate_output(extracted_text, model_choice)

# Function to update visibility based on selected input type
def update_input_fields(input_type):
    if input_type == "Text":
        return gr.Textbox.update(visible=True), gr.File.update(visible=False)
    elif input_type == "PDF":
        return gr.Textbox.update(visible=False), gr.File.update(visible=True)

# Create a Gradio interface
demo = gr.Interface(
    fn=process_input,  # Function to process input
    inputs=[
        gr.Radio(["Text", "PDF"], label="Select input type", interactive=True),  # Radio for choosing input type
        gr.Textbox(label="Enter your text here", visible=True),  # Text input (hidden by default)
        gr.File(label="Upload a PDF", visible=True),  # PDF input (hidden by default)
        gr.Radio(["Gemini", "GPT-2", "Mistral"], label="Choose your model")  # Radio buttons for model selection
    ],
    outputs=gr.Textbox(label="Output teaching transcript"),  # Output type
    title="Teaching Transcript",
    description="Enter a transcript or upload a PDF to transform it into a teaching transcript using Gemini or GPT-2 models.",
)

# Set up the update mechanism for visibility
#demo.input_components[0].change(fn=update_input_fields, inputs=[demo.input_components[0]], outputs=[demo.input_components[1], demo.input_components[2]])

# Launch the Gradio app
demo.launch()

