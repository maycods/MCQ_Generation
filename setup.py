from setuptools import find_packages, setup

setup(
    name="mcq_generator", 
    version="0.1.0", 
    author="Maya Houacine",
    install_requires=["huggingface_hub",
"langchain",
"streamlit",
"gradio",
"python-dotenv",
"pyPDF2",
"transformers",
"accelerate",
"bitsandbytes"],
    packages=find_packages()
    )
