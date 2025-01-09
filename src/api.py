from src.utils import generate_output, extract_text_from_pdf

def process_input(input_type, input_data_text, input_data_pdf, model_choice, temperature, max_n_tokens):

    if input_type == "PDF":
        input_data_text = extract_text_from_pdf(input_data_pdf)
    
    return generate_output(input_data_text, model_choice, temperature, max_n_tokens)
