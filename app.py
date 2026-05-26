from transformers import pipeline
import gradio as gr

# Load GPT-2 model
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Function for story generation
def generate_story(prompt):

    result = generator(
        prompt,
        max_length=120,
        num_return_sequences=1,
        temperature=0.8,
        truncation=True
    )

    return result[0]["generated_text"]


# Gradio Interface
interface = gr.Interface(
    fn=generate_story,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your story prompt here..."
    ),
    outputs="text",
    title="AI Story Generator",
    description="Generate stories using GPT-2"
)

# Launch App
interface.launch()