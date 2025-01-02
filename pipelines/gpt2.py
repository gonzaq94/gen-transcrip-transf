from transformers import pipeline

def call_gpt2(query: str) -> str:

    generator = pipeline("text-generation", model="gpt2")
    gen_text = generator(query, max_new_tokens=9000)

    return gen_text[0]['generated_text'].lstrip(query)
