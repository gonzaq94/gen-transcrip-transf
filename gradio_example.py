import gradio as gr
from transformers import pipeline

# Load a pre-trained sentiment analysis pipeline
sentiment_model = pipeline("sentiment-analysis")
generator = pipeline("text-generation", model="gpt2")

# Define a function to process inputs and generate predictions
def analyze_sentiment(text):
    results = sentiment_model(text)
    return f"Label: {results[0]['label']}, Confidence: {results[0]['score']:.2f}"

# Create a Gradio interface
demo = gr.Interface(
    fn=analyze_sentiment,  # Function to process input
    inputs=gr.Textbox(label="Enter your text here"),  # Input type
    outputs=gr.Textbox(label="Sentiment Analysis Result"),  # Output type
    title="Sentiment Analysis",
    description="Enter a sentence to determine its sentiment (Positive/Negative)."
)

# Launch the Gradio app
demo.launch()
