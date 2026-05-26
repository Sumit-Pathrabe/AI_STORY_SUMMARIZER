from transformers import pipeline

# Load GPT-2 text generation pipeline
generator = pipeline(
    "text-generation",
    model="gpt2"
)
# Function to generate text
def generate_story(prompt):

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1,
        temperature=0.8
    )

    print("\nGenerated Text:\n")
    print(result[0]["generated_text"])
    print("\n" + "="*60)
