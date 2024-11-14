import gradio as gr
from src.mcq_gen.MCQgenerator import generate_evaluate_chain,RESPONSE_JSON
from src.mcq_gen.utils import pdf_Loader,json2df
import json
def qcm_gen(pdf,number,dif):
    
    text= pdf_Loader(pdf)
    response=generate_evaluate_chain(
    {
        "text": text,
        "number": number,
        "difficulty": dif,
        "response_json": json.dumps(RESPONSE_JSON)
    }
    )
    return json2df(response.get("quiz"))

theme = gr.themes.Ocean(primary_hue="teal",
    secondary_hue="cyan",
    neutral_hue="zinc").set(
    
    button_primary_background_fill='*primary_500 ',
    button_primary_background_fill_dark='*primary_500 ',
    button_primary_background_fill_hover='*primary_500',
    button_primary_background_fill_hover_dark='*primary_500 ',
    button_secondary_background_fill='*primary_500 ',
    button_secondary_background_fill_dark='*primary_500 '
)
css = """
h1 {
    text-align: center;
}
"""
with gr.Blocks(title="QCM Generator",css=css) as demo:
    gr.Markdown("""
                # QCM GENERATOR
             
    """)
    with gr.Row():

        pdf= gr.File( file_types=[".pdf"])
        pdf.upload(fn=lambda x:x.name, inputs=pdf, outputs=pdf)
    with gr.Row():
        ex=gr.Examples(examples=["din.pdf"],inputs=pdf)
        
    with gr.Row():
        number = gr.Textbox(label="Number of questions in the QCM:")
    with gr.Row():
        dif = gr.Textbox(label="Level of difficulty:")
    with gr.Row():
        qcm=gr.DataFrame()
    with gr.Row():
        submit_button = gr.Button("Submit")
        submit_button.click(fn=qcm_gen,inputs=[pdf,number,dif],outputs=qcm)

demo.launch()