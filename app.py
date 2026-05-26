from transformers import pipeline
import gradio as gr

# Load GPT-2 pipeline
generator = pipeline(
    "text-generation",
    model="gpt2"
)

# Story generation function
def generate_story(prompt):

    result = generator(
        prompt,
        max_length=120,
        temperature=0.8,
        num_return_sequences=1,
        truncation=True
    )

    return result[0]["generated_text"]


# Gradio UI
interface = gr.Interface(
    fn=generate_story,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter your prompt..."
    ),
    outputs="text",
    title="AI Story Generator",
    description="Generate stories using GPT-2"
)

interface.launch()