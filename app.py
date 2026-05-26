from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline(
    "text-generation",
    model="gpt2"
)
