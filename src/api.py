from src.utils import generate_output, extract_text_from_pdf

def process_input(input_type, input_data_text, input_data_pdf, model_choice):
    if input_type == "Text":
        return generate_output(input_data_text, model_choice)
    elif input_type == "PDF":
        extracted_text = extract_text_from_pdf(input_data_pdf)
        return generate_output(extracted_text, model_choice)
