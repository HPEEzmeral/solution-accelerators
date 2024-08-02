
import gradio as gr
from theme import EzmeralTheme
from chain import simplify_text, explain_term

custom_css = """
footer {visibility: hidden}
"""

title = """
<picture>
  <img alt="Logo" src="https://raw.githubusercontent.com/saradiazdelser/SimplifAI/main/logo.png" style="width: 14%; margin-bottom: 10px;" />
</picture>

# Text Simplification
This application can be used to simplify text to make it more accessible:
"""

# Gradio UI for the fronted
with gr.Blocks(title="HPE - PCAI", theme=EzmeralTheme(), css=custom_css) as demo:
    gr.Markdown(title)

    with gr.Tab("Simplification"):

        input_textbox = gr.Textbox(
            lines=5, placeholder="Put your complicated text here...", label='Complex text'
        )
        submit_butn = gr.Button("Submit", variant="primary")
        output_textbox = gr.Textbox(label = 'Simplified text')

        submit_butn.click(fn=simplify_text, inputs=input_textbox, outputs=output_textbox)

        gr.Markdown("### Get a definition for a concept")

        with gr.Row():
            wd_input_textbox = gr.Textbox(
                lines=1, placeholder="Put a concept that you don't understand here..."
            )
            wd_submit_butn = gr.Button("Submit")
        wd_output_textbox = gr.Textbox()

        wd_submit_butn.click(
            fn=explain_term,
            inputs=[output_textbox, wd_input_textbox],
            outputs=wd_output_textbox,
        )

    with gr.Tab("About the App"):
        try: 
            gr.Markdown(open('INFO.md', 'r').read())
        except:
            print("Couldn't load INFO.md")
        gr.Markdown("Visit the [GitHub](https://github.com/HPEEzmeral/solution-accelerators) for all PCAI Solution Accelerators")


if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")