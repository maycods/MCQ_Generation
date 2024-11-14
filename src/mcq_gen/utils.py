
import gradio as gr
from langchain_community.document_loaders import PyPDFLoader
import pandas as pd
import json

def json2df(quiz):
    quiz=json.loads(quiz)
    quiz_table_data = []
    for key, value in quiz.items():
        mcq = value["mcq"]
        options = " | ".join(
            [
                f"{option}: {option_value}"
                for option, option_value in value["options"].items()
                ]
            )
        correct = value["correct"]
        quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
    return pd.DataFrame(quiz_table_data)

def pdf_Loader(pdf):
    loader = PyPDFLoader(pdf)
    pages = []
    for page in loader.load():
        pages.append(page)

    text= "\n".join([page.page_content for page in pages])
    return text
