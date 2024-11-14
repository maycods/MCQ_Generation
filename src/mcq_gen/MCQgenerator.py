import os
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import AI21
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import AI21
from dotenv import load_dotenv
## Inputs
TEMPLATE1="You are an expert in english i want you to extract the subject of this text: {text}. The subject should be composed of 1 or 2 words without comma"
TEMPLATE="""
Text:{text}
You are an expert MCQ maker. Given the above text, it is your job to \
create a quiz  of {number} multiple choice questions for {subject} students with a {difficulty} level of difficulty . 
Make sure the questions are short and not repeated and check all the questions to be conforming the text as well.
Make sure to format your response like  RESPONSE_JSON below and use it as a guide. \
Ensure to make {number} MCQs and to follow the RESPONSE_JSON format
### RESPONSE_JSON
{response_json}

"""
RESPONSE_JSON = {
    "1": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
    "2": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
    "3": {
        "mcq": "multiple choice question",
        "options": {
            "a": "choice here",
            "b": "choice here",
            "c": "choice here",
            "d": "choice here",
        },
        "correct": "correct answer",
    },
}

load_dotenv()
key =  os.getenv("AI21_API_KEY")
ai21 = AI21(ai21_api_key=key, model="j2-jumbo-instruct")

subject_extraction_prompt=PromptTemplate(input_variables=["text"], template=TEMPLATE1)
subject_chain=LLMChain(llm=ai21, prompt=subject_extraction_prompt, output_key="subject")

quiz_generation_prompt = PromptTemplate(
    input_variables=["text", "number", "subject", "difficulty", "response_json"],
    template=TEMPLATE
    )
quiz_chain=LLMChain(llm=ai21, prompt=quiz_generation_prompt, output_key="quiz")


generate_evaluate_chain=SequentialChain(chains=[subject_chain,quiz_chain], input_variables=["text", "number", "difficulty", "response_json"],
                                        output_variables=["subject","quiz"])
