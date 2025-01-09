import gradio as gr
from huggingface_hub import InferenceClient
from src.api import process_input

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

# Function to update visibility based on selected input type
def update_input_fields(input_type):
    if input_type == "Text":
        return gr.Textbox.update(visible=True), gr.File.update(visible=False)
    elif input_type == "PDF":
        return gr.Textbox.update(visible=False), gr.File.update(visible=True)

# Create a Gradio interface
interface = gr.Interface(
    fn=process_input,  # Function to process input
    inputs=[
        gr.Radio(["Text", "PDF"], label="Select input type", interactive=True),  # Radio for choosing input type
        gr.Textbox(label="Enter your text here", visible=True),  # Text input (hidden by default)
        gr.File(label="Upload a PDF", visible=True),  # PDF input (hidden by default)
        gr.Radio(["Gemini", "Mistral", "GPT"], label="Choose your model"),  # Radio buttons for model selection
        gr.Slider(minimum=0, maximum=1, step=0.01, value=0.7, label="Select Temperature"),  # Slider for temperature
        gr.Number(value=3900, label="Target min number of generated words")  # New field for min number of words with default value
    ],
    outputs=gr.Textbox(label="Output teaching transcript"),  # Output type
    title="Teaching Transcript",
    description="Enter a transcript or upload a PDF to transform it into a teaching transcript using LLMs.",
)

# Set up the update mechanism for visibility
#interface.input_components[0].change(fn=update_input_fields, inputs=[interface.input_components[0]], outputs=[interface.input_components[1], interface.input_components[2]])

if __name__ == "__main__":
    interface.launch()